from functools import reduce


def soma(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    lista = [47, 11, 79, 42, 13]

    print(f"\n{lista}")

    print(f"\nSomatório de {lista} = {reduce(soma, lista)}")

    print(f"\nSomatório de {lista} = {reduce(lambda x, y: x + y, lista)}")

    max_find = lambda a, b: a if a > b else b

    print(f"\nTipo de max_find = {type(max_find)}")

    print(f"\nMaior entre {lista} = {reduce(max_find, lista)}")
