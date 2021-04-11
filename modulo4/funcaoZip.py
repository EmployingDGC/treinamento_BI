def trocaValores(d1: dict, d2: dict) -> dict:
    dic_temp = {}

    for d1key, d2val in zip(d1, d2.values()):
        dic_temp[d1key] = d2val

    return dic_temp


if __name__ == "__main__":
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]

    print(f"\nResultado zip: {list(zip(lista1, lista2))}")

    lista3 = [1, 2, 3]
    lista4 = [4, 5, 6, 7, 8]

    print(f"\nResultado zip: {list(zip(lista3, lista4))}")

    dicionario1 = {"a": 1, "b": 2}
    dicionario2 = {"c": 3, "d": 4}

    print(f"\nResultado zip: {list(zip(dicionario1, dicionario2))}")
    print(f"Resultado zip: {list(zip(dicionario1, dicionario2.values()))}")
    print(f"Resultado zip: {list(zip(dicionario1.values(), dicionario2.values()))}")

    print(f"\nTrocando valores: {trocaValores(dicionario1, dicionario2)}")
