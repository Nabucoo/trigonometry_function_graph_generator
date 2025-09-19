import questionary
import numpy as np
import math

#cria 200 pontos de x entre -1 e 1



def main():
    print("-------------------------------------------")
    print("Gerador de gráficos de funções seno/cosseno")
    print("-------------------------------------------")

    while True:
        #pergunta qual o tipo de função
        type_function = questionary.select(
            "Qual tipo de função você deseja calcular: ",
            choices = ["Função cosseno", "Funçao seno"]
        ).ask()

        #a e b devem ser diferentes de zero, então, fazemos um loop para garantir isso
        #também tratamos os erros para caso o usuário digite algo diferente de float, uma caracter ou algo do tipo.
        print("Os valores de a e b devem ser diferentes de zero, pois senão, será uma função constante!")
        try:
            a, b = 0, 0

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
        x = np.linspace(-1 * abs(a) + d, 1 * abs(a) + d, 200)
        #quando a função e cosseno e seno, o y muda, aqui colocamos a fórmula.

        #a variavel "y" sera a saida
        if type_function == "Função cosseno":
            y = a * math.cos(b*x + c) + d
            if c < 0:
                c = f"-{abs(c)}"
            if d < 0:
                d = f"-({abs(d)})"
            formula = f"{a} · cos({b}X + {c} ) · {d}"

        elif type_function == "Função seno":
            y = a * math.sen(b*x + c) + d
            if c < 0:
                c = f"-{abs(c)}"
            if d < 0:
                d = f"-({abs(d)})"
            formula = f"{a} · sen({b}X + {c} ) · {d}"

        else:
            print("Erro, por favor selecione uma opção válida!")
            continue

main()