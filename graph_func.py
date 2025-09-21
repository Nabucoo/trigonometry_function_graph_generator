import questionary
import numpy as np
import matplotlib.pyplot as plt  # import para o gráfico
import math

def main():
    print("-------------------------------------------")
    print("Gerador de gráficos de funções seno/cosseno")
    print("-------------------------------------------")

    while True:
        type_function = questionary.select(
            "Qual tipo de função você deseja calcular: ",
            choices=["Função cosseno", "Função seno"]
        ).ask()

        print("Os valores de a e b devem ser diferentes de zero, pois senão, será uma função constante!")
        try:
            a, b = 0, 0

            while a == 0:
                a = float(input("Digite o valor de A(amplitude): "))
            while b == 0:
                b = float(input("Digite o valor de B(controle de frequência): "))

            c = float(input("Digíte o valor de C(deslocamento horizontal): "))
            d = float(input("Digíte o valor de D(deslocamento vertical): "))
        except Exception as e:
            print("Valores inválidos!")
            continue

        print(a, b, c, d)
        x = np.linspace(-10, 10, 500)  # mais pontos para ver melhor o gráfico

        if type_function == "Função cosseno":
            y = a * np.cos(b * x + c) + d
            formula = f"{a} · cos({b}x + {c}) + {d}"

        elif type_function == "Função seno":
            y = a * np.sin(b * x + c) + d
            formula = f"{a} · sin({b}x + {c}) + {d}"

        else:
            print("Erro, por favor selecione uma opção válida!")
            continue

        # --- Adicionando o gráfico no plano cartesiano ---
        plt.axhline(0, color="black", linewidth=1)  # eixo x
        plt.axvline(0, color="black", linewidth=1)  # eixo y
        plt.plot(x, y, label=formula)
        plt.title("Gráfico da função")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.show()

main()