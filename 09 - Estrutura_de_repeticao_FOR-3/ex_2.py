# 2. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 < num2:  # Verifica se num1 é menor que num2
    for i in range(num1, num2 - 1):
        i = i + 1  # Incrementa 1 para que o programa imprima o intervalo dos números SEM incluir o próprio número.
        print(i)

elif num2 < num1:  # Verifica se num2 é menor que num1
    for i in range(num2, num1 - 1):
        i = i + 1  # Incrementa 1 para que o programa imprima o intervalo dos números SEM incluir o próprio número.
        print(i)
else:
    print("Não há intervalo entre os números.")