import os
import sqlite3


if __name__ == "__main__":
    db_file = "databases/escola.db"

    os.remove(db_file) if os.path.exists(db_file) else None

    con = sqlite3.connect(db_file)

    cur = con.cursor()

    cur.execute(
        f"create table cursos ("
        f"id integer primary key,"
        f"titulo varchar(100),"
        f"categoria varchar(140)"
        f")"
    )

    cur.execute(
        f"insert into cursos values"
        f"(1, 'Ciência de Dados', 'Data Science'),"
        f"(2, 'Big Data Fundamentos', 'Big Data'),"
        f"(3, 'Python Fundamentos', 'Análise de Dados')"
    )

    con.commit()

    cur.execute(
        f"select * from cursos"
    )

    data = cur.fetchall()

    print(f"+{'-' * 74}+")
    print(f"| {'ID':^6} | {'TÍTULO':^30} | {'CATEGORIA':^30} |")
    print(f"+{'-' * 74}+")

    for id_curso, titulo, categoria in data:
        print(f"| {id_curso:06} | {titulo:<30} | {categoria:<30} |")

    print(f"+{'-' * 74}+")

    con.close()
