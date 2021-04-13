from pymongo import MongoClient
from pymongo import errors
from datetime import datetime

if __name__ == "__main__":
    connection = MongoClient("localhost", 27017)

    db = connection.cadastrodb

    try:
        db.create_collection("minhacollection")
    except errors.CollectionInvalid:
        pass

    print(f"\n{db.list_collection_names}")

    db.minhacollection.insert_one({
        "titulo": "MongoDB com Python",
        "descricao": "MongoDB é um banco de Dados NoSQL",
        "by": "Data Science Academy",
        "url": "http://www.datascienceacademy.com.br",
        "tags": ["mongodb", "databases", "NoSQL"],
        "likes": 100
    })

    print(f"\n{db.list_collection_names}")

    for line in db.minhacollection.find():
        print(f"{line}")
