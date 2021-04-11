if __name__ == "__main__":
    file = open("./arquivos/salarios.csv", "r")
    data = file.read()
    rows = data.split("\n")
    full_data = []

    for row in rows:
        split_row = row.split(",")
        full_data.append(split_row)

    new_full_data = []

    for row in full_data:
        try:
            new_full_data.append([row[-1], row[-2]])
        except:
            pass

    salary = []

    for row in new_full_data:
        salary.append(row[0])

    s_sort = []

    for s in salary:
        try:
            s_sort.append(float(s[1:]))
        except:
            pass

    s_sort.sort()

    for s in s_sort:
        print(s)
