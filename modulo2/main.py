# funções built-in https://docs.python.org/pt-br/3/library/functions.html

if __name__ == '__main__':

    string = "uma frase legal"
    nome = "davi"

    print(f"\nUsando slice\n")

    print(f"string[:]    = {string[:]}")
    print(f"string[:1]   = {string[:1]}")
    print(f"string[:2]   = {string[:2]}")
    print(f"string[1:]   = {string[1:]}")
    print(f"string[2:]   = {string[1:]}")
    print(f"string[:-1]  = {string[:-1]}")
    print(f"string[:-2]  = {string[:-2]}")
    print(f"string[::1]  = {string[::1]}")
    print(f"string[::2]  = {string[::2]}")
    print(f"string[::-1] = {string[::-1]}")
    print(f"string[::-2] = {string[::-2]}")

    print(f"\nOperadores com string\n")

    print(f"string[2] * 5   = {string[2] * 5}")
    print(f"string[2] + '5' = {string[2] + '5'}")

    print(f"\nMétodos de string\n")

    print(f"string.upper()       = {string.upper()}")
    print(f"string.lower()       = {string.lower()}")
    print(f"string.split()       = {string.split()}")
    print(f"string.upper(\" \")    = {string.split(' ')}")
    print(f"string.upper(\"a\")    = {string.split('a')}")
    print(f"string.capitalize()  = {string.capitalize()}")
    print(f"string.count(\"a\")    = {string.count('a')}")
    print(f"string.find(\"a\")     = {string.find('a')}")
    print(f"string.islower()     = {string.islower()}")
    print(f"string.isspace()     = {string.isspace()}")
    print(f"string.endswith(\"a\") = {string.endswith('a')}")
    print(f"string.endswith(\"l\") = {string.endswith('l')}")

    print(f"\nComparação de strings\n")

    print(f"string == nome              = {string == nome}")
    print(f"string == \"uma frase legal\" = {string == 'uma frase legal'}")
    print(f"string == \"Davi\"            = {string == 'Davi'}")

    print(f"\nListas\n")

    lista = ["Banana", "Abacate", "Pera", "Uva"]

    print(f"[\"Banana\", 5, \"Maçã\", 10] = {['Banana', 5, 'Maçã', 10]}")
    print(f"lista                     = {lista}")
    print(f"lista[:]                  = {lista[:]}")
    print(f"lista[1:0]                = {lista[1:0]}")
    print(f"lista[1:3]                = {lista[1:3]}")
    print(f"lista[0:2]                = {lista[0:2]}")
    print(f"lista[::-1]               = {lista[::-1]}")
    print(f"lista[0]                  = {lista[0]}")

    del lista[2]
    print(f"del lista[2]              = {lista}")

    lista.append("Pera")
    print(f"lista.append(\"Pera\")      = {lista}")

    print(f"lista.count(\"Pera\")       = {lista.count('Pera')}")
    print(f"lista.count(\"pera\")       = {lista.count('pera')}")

    print(f"\nLista de Lista\n")

    lista_de_lista = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10, 11, 12]]

    print(f"lista_de_lista       = {lista_de_lista}")
    print(f"lista_de_lista[0][2] = {lista_de_lista[0][2]}")

    print(f"\nMatriz \"Sparsa\":")
    for linha in lista_de_lista:
        print(f"\t", end="")
        for coluna in linha:
            print(f"{coluna} ", end="")
        print()

    print(f"\nOperador in\n")

    print(f"[1, 2, 3, 4] in lista_de_lista = {[1, 2, 3, 4] in lista_de_lista}")
    print(f"9 in lista_de_lista[2]         = {9 in lista_de_lista[2]}")

    print(f"\nFunções built-in para Listas\n")

    print(f"len(lista_de_lista)          = {len(lista_de_lista)}")
    print(f"len(lista_de_lista[0])       = {len(lista_de_lista[0])}")
    print(f"len(lista_de_lista[1])       = {len(lista_de_lista[1])}")
    print(f"len(lista_de_lista[2])       = {len(lista_de_lista[2])}")
    print(f"max(lista_de_lista)          = {max(lista_de_lista)}")
    print(f"max(lista_de_lista[0])       = {max(lista_de_lista[0])}")
    print(f"max(lista_de_lista[1])       = {max(lista_de_lista[1])}")
    print(f"max(lista_de_lista[2])       = {max(lista_de_lista[2])}")
    print(f"min(lista_de_lista)          = {min(lista_de_lista)}")
    print(f"min(lista_de_lista[0])       = {min(lista_de_lista[0])}")
    print(f"min(lista_de_lista[1])       = {min(lista_de_lista[1])}")
    print(f"min(lista_de_lista[2])       = {min(lista_de_lista[2])}")

    print(f"\nContinuando com Listas\n")

    lista.extend(lista_de_lista)

    print(f"lista.extend(lista_de_lista) = {lista}")

    lista.remove([1, 2, 3, 4])
    print(f"lista.remove([1, 2, 3, 4])   = {lista}")

    lista.reverse()
    print(f"lista.reverse()              = {lista}")

    lista[0].sort()  # só pode ser ordenada as listas que possuem tipos únicos
    print(f"lista[0].sort()              = {lista}")

    lista[1].sort(reverse=True)  # só pode ser ordenada as listas que possuem tipos únicos
    print(f"lista[1].sort(reverse=True)  = {lista}")

    print(f"\nDicionários\n")

    dicionario = {"abacate": "fruta", 1: "numero", "tomate": "fruta"}

    print(f"\u007b\"abacate\": \"fruta\", 1: \"numero\", \"tomate\": \"fruta\"\u007d  = {dicionario}")
    print(f"dicionario[1]                                         = {dicionario[1]}")
    print(f"dicionario[\"abacate\"]                                 = {dicionario['abacate']}")

    dicionario["cadeira"] = "objeto"
    print(f"dicionario[\"cadeira\"] = \"objeto\"                      = {dicionario}")

    print(f"dicionario.keys()                                     = {dicionario.keys()}")
    print(f"dicionario.values()                                   = {dicionario.values()}")
    print(f"dicionario.items()                                    = {dicionario.items()}")

    dicionario.update({"joaquim": "pessoa", 5: "numero"})
    print(f"dicionario.update(\u007b\"joaquim\": \"pessoa\", 5: \"numero\"\u007d) = {dicionario}")
