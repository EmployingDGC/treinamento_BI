import sqlite3
import datetime
import random
import matplotlib.pyplot as plt


if __name__ == "__main__":
    db_file = "databases/dsa.db"

    connection = sqlite3.connect(db_file)

    cursor = connection.cursor()

    cursor.execute(
        f"create table if not exists produtos ( "
        f"    id_produto integer primary key autoincrement not null, "
        f"    dt_compra text, "
        f"    nm_produto text, "
        f"    vl_valor real "
        f"); "
    )

    cursor.execute(
        f"insert into produtos ( "
        f"    dt_compra, "
        f"    nm_produto, "
        f"    vl_valor "
        f")"
        f"values"
        f"    ('{datetime.datetime.now()}', 'teclado', 130)"
    )

    connection.commit()

    cursor.execute(
        f"select "
        f"    id_produto, "
        f"    vl_valor "
        f"from "
        f"    produtos "
        f";"
    )

    ids = []
    valores = []
    data = cursor.fetchall()

    for id_produto, valor in data:
        ids.append(id_produto)
        valores.append(valor)

    plt.bar(ids, valores)
    plt.show()
