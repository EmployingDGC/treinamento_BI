if __name__ == "__main__":
    lista_caracteres = [x for x in "um valor qualquer"]

    print(f"\nLista de caracteres: {lista_caracteres}")

    lista_quadrado = [x ** 2 for x in range(10)]

    print(f"\nLista {list(range(10))} ao quadrado: {lista_quadrado}")

    lista_pares = [x for x in range(10) if x % 2 == 0]

    print(f"\nLista {list(range(10))} só com pares: {lista_pares}")

    celsius = [0, 10, 20.1, 34.5]

    fahrenheit = [(t * 9.0 / 5.0) + 32 for t in celsius]

    print(f"\nTemperaturas {celsius} em fahrenheit: {fahrenheit}")

    list_comprehension_aninhadas = [x ** 2 for x in [z ** 2 for z in range(1, 11)]]

    print(f"\nList Comprehension aninhadas: {list_comprehension_aninhadas}")
