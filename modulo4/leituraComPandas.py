import pandas as pd

if __name__ == "__main__":
    file = "./arquivos/salarios.csv"

    print(pd.read_csv(file).head())
