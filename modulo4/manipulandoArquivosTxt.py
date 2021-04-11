import os

if __name__ == "__main__":
    texto = "Cientista de Dados é a profissão que mais tem crescido em todo mundo.\n"
    texto += "Esses profissionais precisam se especializar em Programação, Estatística e Machine Learning.\n"
    texto += "E claro, em Big Data"

    print(f"\n\n{texto}")

    file = open(os.path.join("./arquivos/cientista.txt"), "w")

    for palavra in texto.split():
        file.write(f"{palavra} ")

    file.close()

    file = open("./arquivos/cientista.txt", "r")
    conteudo = file.read()
    file.close()

    print(f"\n\n{conteudo}")

    with open("./arquivos/cientista.txt", "w") as arqivo:
        arqivo.write(texto[:21])
        arqivo.write('\n')
        arqivo.write(texto[:33])

    with open("./arquivos/cientista.txt", "r") as arqivo:
        conteudo = arqivo.read()

    print(f"\n\n{conteudo}")
