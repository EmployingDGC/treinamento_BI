import json
from urllib.request import urlopen

if __name__ == "__main__":
    dicionario = {
        "nome": "Guido Van Rossum",
        "linguagem": "Python",
        "similar": ["c", "Modular-3", "Lisp"],
        "users": 1000000
    }

    for k, v in dicionario.items():
        print(f"{k:<10} -> {v}")

    with open("./arquivos/dados.json", "w") as file:
        file.write(json.dumps(dicionario))

    with open("./arquivos/dados.json", "r") as file:
        text = file.read()
        data = json.loads(text)

    print(f"\n{data}")
    print(f"{data['nome']}")

    response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read()
    data = json.loads(response)[0]

    print(f"\nTítulo: {data['title']}")
    print(f"URL: {data['url']}")
    print(f"Duração: {data['duration']}min")
    print(f"Número de Visualizações: {data['stats_number_of_plays']}")

    arquivo_fonte = "./arquivos/dados.json"
    arquivo_destino = "./arquivos/json_data.txt"

    with open(arquivo_fonte, "r") as file_in:
        text = file_in.read()
        with open(arquivo_destino, "w") as file_out:
            file_out.write(text)

    with open("./arquivos/json_data.txt", "r") as file:
        text = file.read()
        data = json.loads(text)

    print(f"\n{data}")
