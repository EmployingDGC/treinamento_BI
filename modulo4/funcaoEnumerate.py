if __name__ == "__main__":
    lista1 = ["a", "b", "c"]

    print(f"\nlista1 enumerada: {list(enumerate(lista1))}")

    dicionario1 = {}

    for indice, valor in enumerate(lista1):
        dicionario1[indice] = valor

    print(f"\nConversão da lista enumerada para dicionário: {dicionario1}")
