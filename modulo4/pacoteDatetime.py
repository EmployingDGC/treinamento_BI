import datetime

if __name__ == "__main__":
    agora = datetime.datetime.now()

    print(f"\n{agora}")

    minha_hora = datetime.time(15, 30, 45)

    print(f"\n{minha_hora}")

    print(f"{'Horas':-<13}: {minha_hora.hour}")
    print(f"{'Minutos':-<13}: {minha_hora.minute}")
    print(f"{'Segundos':-<13}: {minha_hora.second}")
    print(f"{'Microsegundos':-<13}: {minha_hora.microsecond}")

    date1 = datetime.date(2015, 4, 28)

    print(f"\ndate1: {date1}")

    date2 = date1.replace(year=2021)

    print(f"date2: {date2}")

    print(f"date2 - date1 = {str(date2 - date1).replace('days', 'dias')}")
