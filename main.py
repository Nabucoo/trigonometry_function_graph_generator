import questionary
import numpy as np
import math

x = np.linspace(-1, 1, 200)

def main():
    print("-------------------------------------------")
    print("Gerador de gráficos de funções seno/cosseno")
    print("-------------------------------------------")

    while True:
        type_function = questionary.select(
            "Qual tipo de função você deseja calcular: ",
            choices = ["Função cosseno", "Funçao seno"]
        ).ask()

        print("Os valores de a e b devem ser diferentes de zero, pois senão, será uma função constante!")
        try:
            a = 0
            b = 0
            while a == 0:
                a = float(input("Digite o valor de A(amplitude): "))
            while b == 0:
                b = float(input("Digite o valor de B(controle de frequência): "))

            c = float(input("Digíte o valor de C(deslocamento horizoontal): "))
            d = float(input("Digíte o valor de D(deslocamento vertical): "))
        except Exception as e:
            print("Valores inválidos!")
            continue

        
        print(a, b, c, d)

        if type_function == "Função cosseno":
            y = a * math.cos(b*x + c) + d    
        elif type_function == "Função seno":
            y = a * math.sen(b*x + c) + d
        else:
            print("Erro, por favor selecione uma opção válida!")
            continue

main()