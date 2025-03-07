# 1. Solicite ao usuário um número inteiro positivo e exiba apenas os números pares de 2 até esse número.

contador = 0
num = int(input("Digite um número: "))

while True: # o while true é uma estrutura de repetição que funciona indepentente de qualquer coisa até o comando break seja ativado.
    contador += 2 # o contador incrementa de 2 em 2 e depois é printado
    print(contador)
    if contador == num: # se o contador chegar no número inserido, o programa se encerra.
        break