from random import choices


def ehPar(x: int) -> bool:
    return True if x % 2 == 0 else False


def ehImpar(x: int) -> bool:
    return True if x % 2 != 0 else False


if __name__ == "__main__":
    valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    pares = list(filter(ehPar, valores))
    impares = list(filter(ehImpar, valores))

    print(f"\nTodos os valores: {valores}")
    print(f"\nValores pares: {list(filter(ehPar, valores))}")
    print(f"\nValores impares: {list(filter(ehImpar, valores))}")

    valores2 = choices(range(1000), k=15)

    print(f"\nTodos os valores: {valores2}")
    print(f"\nValores pares: {list(filter(lambda x: x % 2 == 0, valores2))}")
    print(f"\nValores impares: {list(filter(lambda x: x % 2 != 0, valores2))}")
