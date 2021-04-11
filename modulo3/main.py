
# calculadora

def soma(x: float, y: float) -> float:
    return x + y


def subtracao(x: float, y: float) -> float:
    return x - y


def multiplicacao(x: float, y: float) -> float:
    return x * y


def divisao(x: float, y: float) -> float:
    return x / y


if __name__ == '__main__':
    while True:
        print(f"+{'-' * 30}+")
        print(f"|{'MENU':^30}|")
        print(f"+{'-' * 30}+")
        print(f"| 1 | {'Soma':<24} |")
        print(f"| 2 | {'Subtração':<24} |")
        print(f"| 3 | {'Multiplicação':<24} |")
        print(f"| 4 | {'Divisão':<24} |")
        print(f"| 0 | {'Sair':<24} |")
        print(f"+{'-' * 30}+")
        opcao = input("Digite uma das opções acima: ")

        if opcao == "0":
            break

        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))

        print()

        if opcao == "1":
            print(f"{x} \u002b {y} = {soma(x, y)}")

        elif opcao == "2":
            print(f"{x} \u2212 {y} = {subtracao(x, y)}")

        elif opcao == "3":
            print(f"{x} \u00d7 {y} = {multiplicacao(x, y)}")

        elif opcao == "4":
            print(f"{x} \u00f7 {y} = {divisao(x, y)}")
