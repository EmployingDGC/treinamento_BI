import os
import sqlite3
from datetime import datetime


if __name__ == "__main__":
    db_file = "databases/dsa.db"

    os.remove(db_file) if os.path.exists(db_file) else None

    connection = sqlite3.connect(db_file)

    cursor = connection.cursor()

    cursor.execute(
        f"create table produtos ( "
        f"    id_produto integer primary key autoincrement not null, "
        f"    dt_compra text, "
        f"    nm_produto text, "
        f"    vl_valor real "
        f"); "
    )

    connection.commit()

    cursor.execute(
        f"insert into produtos ( "
        f"    dt_compra, "
        f"    nm_produto, "
        f"    vl_valor "
        f") "
        f"values "
        f"    ('{datetime.now()}', 'teclado', 90.0), "
        f"    ('{datetime.now()}', 'mouse', 145.5), "
        f"    ('{datetime.now()}', 'monitor', 750.0), "
        f"    ('{datetime.now()}', 'headset', 170.0), "
        f"    ('{datetime.now()}', 'rx580', 2000.0) "
        f";"
    )

    connection.commit()

    cursor.execute(
        f"select "
        f"    * "
        f"from "
        f"    produtos "
        f";"
    )

    data = cursor.fetchall()

    print(f"\n{'Imprimindo todos os produtos':^89}")
    print(f"+{'-' * 87}+")
    print(f"| {'ID':^6} | {'DT_COMPRA':^30} | {'NM_PRODUTO':^30} | {'VL_VALOR':^10} |")
    print(f"+{'-' * 87}+")

    for id_produto, dt_compra, nm_produto, vl_valor in data:
        print(f"| {id_produto:06} | {dt_compra:^30} | {nm_produto:<30} | {vl_valor:>10.2f} |")

    print(f"+{'-' * 87}+")

    cursor.execute(
        f"select "
        f"    sum(vl_valor) "
        f"from "
        f"    produtos "
        f";"
    )

    data = cursor.fetchall()

    print(f"\n{'Imprimindo soma dos valores de todos os produtos':<89}")
    print(f"+{'-' * 12}+")
    print(f"| {'SUM':^10} |")
    print(f"+{'-' * 12}+")

    print(f"| {data[0][0]:>10.2f} |")

    print(f"+{'-' * 12}+")

    cursor.execute(
        f"update "
        f"    produtos "
        f"set "
        f"    vl_valor = 700.0 "
        f"where "
        f"    id_produto = 3 "
        f";"
    )

    connection.commit()

    cursor.execute(
        f"select "
        f"    * "
        f"from "
        f"    produtos "
        f"where "
        f"    id_produto = 3"
        f";"
    )

    data = cursor.fetchall()

    print(f"\n{'Imprimindo somente o id 3 depois de alterar seu valor':^89}")
    print(f"+{'-' * 87}+")
    print(f"| {'ID':^6} | {'DT_COMPRA':^30} | {'NM_PRODUTO':^30} | {'VL_VALOR':^10} |")
    print(f"+{'-' * 87}+")

    for id_produto, dt_compra, nm_produto, vl_valor in data:
        print(f"| {id_produto:06} | {dt_compra:^30} | {nm_produto:<30} | {vl_valor:>10.2f} |")

    print(f"+{'-' * 87}+")

    cursor.execute(
        f"delete from "
        f"    produtos "
        f"where "
        f"    id_produto = 3 "
        f";"
    )

    connection.commit()

    cursor.execute(
        f"select "
        f"    * "
        f"from "
        f"    produtos "
        f";"
    )

    data = cursor.fetchall()

    print(f"\n{'Imprimindo todos os produtos depois de remover o id 3':^89}")
    print(f"+{'-' * 87}+")
    print(f"| {'ID':^6} | {'DT_COMPRA':^30} | {'NM_PRODUTO':^30} | {'VL_VALOR':^10} |")
    print(f"+{'-' * 87}+")

    for id_produto, dt_compra, nm_produto, vl_valor in data:
        print(f"| {id_produto:06} | {dt_compra:^30} | {nm_produto:<30} | {vl_valor:>10.2f} |")

    print(f"+{'-' * 87}+")

    cursor.close()
    connection.close()
