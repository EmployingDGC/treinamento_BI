def fahrenheit(t: float) -> float:
    return (t * 9.0 / 5.0) + 32


def celsius(t: float) -> float:
    return (t - 32) * 5.0 / 9.0


if __name__ == "__main__":
    temperaturas = [0, 22.5, 40, 100]

    convertidas = list(map(fahrenheit, temperaturas))

    print(f"\n{convertidas}")

    convertidas = list(map(celsius, temperaturas))

    print(f"\n{convertidas}")

    lista1 = [1, 2, 3, 4]
    lista2 = [5, 6, 7, 8]
    lista3 = [9, 10, 11, 12]

    somaElementosListas = list(map(lambda x, y, z: x + y + z, lista1, lista2, lista3))

    print(f"\nlista resultante: {somaElementosListas}")
