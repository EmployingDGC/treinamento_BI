import datetime


class Livro:
    def __init__(self, titulo: str, isbn: int) -> None:
        self._titulo = titulo
        self._isbn = isbn

    def getTitulo(self) -> str:
        return self._titulo

    def getIsbn(self) -> int:
        return self._isbn

    def getInfo(self) -> dict:
        return {
            "nome": self.getTitulo(),
            "isbn": self.getIsbn()
        }


class Cachorro:
    def __init__(self, nome: str, raca: str, nascimento: datetime.date) -> None:
        self._nome = nome
        self._raca = raca
        self._nascimento = nascimento
        self._idade = (datetime.date.today() - nascimento).days

    def getNome(self) -> str:
        return self._nome

    def getRaca(self) -> str:
        return self._raca

    def getNascimento(self) -> str:
        return f"{self._nascimento.day}/{self._nascimento.month}/{self._nascimento.year}"

    def getIdade(self) -> int:
        return self._idade


if __name__ == "__main__":
    meu_livro = Livro("O monge e o Executivo", 9988888)

    print(f"\nTodas as Infos: {meu_livro.getInfo()}")
    print(f"Título: {meu_livro.getTitulo()}")
    print(f"ISBN: {meu_livro.getIsbn()}")

    meu_cachorro = Cachorro("Nala", "PittBull", datetime.date(2020, 10, 28))

    print(f"\nNome: {meu_cachorro.getNome()}")
    print(f"Raça: {meu_cachorro.getRaca()}")
    print(f"Idade: {meu_cachorro.getIdade()} dias")
    print(f"Nascimento: {meu_cachorro.getNascimento()}")
