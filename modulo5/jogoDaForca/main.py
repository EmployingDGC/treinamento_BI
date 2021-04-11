# -*- coding: utf-8 -*-
from random import choices


class Hangman:
    def __init__(self, word: str) -> None:
        self._word = word.upper()
        self._hide_word = ["_" if letter.isalpha() else letter if letter != "_" else "-" for letter in word]
        self._typed_letters = []
        self._correct_letters = []
        self._wrong_letters = []

    def get_correct_letters(self) -> str:
        return ", ".join(self._correct_letters)

    def get_wrong_letters(self) -> str:
        return ", ".join(self._wrong_letters)

    def get_word(self) -> str:
        return self._word

    def guess(self, letter: str) -> bool:
        is_found = False
        letter_upper = letter.upper()

        if not letter_upper.isalpha() or len(letter_upper) != 1 or letter_upper in self._typed_letters:
            return is_found

        for i, l in enumerate(self._word):
            if letter_upper == l:
                self._hide_word[i] = letter_upper
                is_found = True

        self._typed_letters.append(letter_upper)

        if is_found:
            self._correct_letters.append(letter_upper)

        else:
            self._wrong_letters.append(letter_upper)

        return is_found

    def hangman_over(self) -> bool:
        return len(self._wrong_letters) > 6

    def hangman_won(self) -> bool:
        return "_" not in self._hide_word

    def end_game(self) -> bool:
        return self.hangman_won() or self.hangman_over()

    def get_board(self) -> str:
        doll = []
        len_doll = len(self._wrong_letters)
        hide_word = ''.join(self._hide_word)
        len_hide_word = len(hide_word)

        doll.append("O" if len_doll > 0 else " ")
        doll.append("/" if len_doll > 1 else " ")
        doll.append("|" if len_doll > 2 else " ")
        doll.append("\\" if len_doll > 3 else " ")
        doll.append("|" if len_doll > 4 else " ")
        doll.append("/" if len_doll > 5 else " ")
        doll.append("\\" if len_doll > 6 else " ")

        return (
            f"\n+---------+" +
            f"\n|         |" +
            f"\n|         {doll[0]}" +
            f"\n|        {doll[1]}{doll[2]}{doll[3]}" +
            f"\n|         {doll[4]}" +
            f"\n|        {doll[5]} {doll[6]}" +
            f"\n|" +
            f"\n|" +
            f"\n| ({len_hide_word}) {hide_word}" +
            f"\n======{'=' * 17 if len_hide_word < 18 else '=' * len_hide_word}" +
            f"\nLetras Corretas: {self.get_correct_letters()}"
            f"\n"
            f"\nLetras Erradas: {self.get_wrong_letters()}"
        )


def rand_word() -> str:
    words = []

    try:
        with open("./palavras.txt", "r") as file:
            words = [w for w in file.readlines()]
    except FileNotFoundError:
        pass

    try:
        word = choices(words, k=1)[0]
    except IndexError:
        word = "nenhuma palavra encontrada no arquivo"

    return word.strip()


def play():
    game = Hangman(rand_word())

    while not game.end_game():
        print(game.get_board())

        letter = input("\nDigite uma letra: ")

        game.guess(letter)

    print(game.get_board())

    if game.hangman_won():
        print(f"\nParabéns! Você ganhou!")

    else:
        print(f"\nInfelizmente, você perdeu!")
        print(f"A palavra era {game.get_word()}")


if __name__ == "__main__":
    play()
