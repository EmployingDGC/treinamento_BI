import csv

if __name__ == "__main__":
    with open("./arquivos/numeros.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(("primeira", "segunda", "terceira"))
        writer.writerow((55, 93, 76))
        writer.writerow((62, 14, 86))

    print("\n\n")

    with open("./arquivos/numeros.csv", "r") as file:
        reader = csv.reader(file)
        for x in reader:
            print(f"\nNúmero de colunas: {len(x)}\n{x}")

    print("\n\n")

    with open("./arquivos/numeros.csv", "r") as file:
        reader = csv.reader(file)
        data = list(reader)

    print(data)

    print("\n\n")
