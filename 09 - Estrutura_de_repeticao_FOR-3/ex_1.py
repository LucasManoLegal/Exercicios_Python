# 1. Faça um programa que leia 5 números e informe o maior número.

lista = []
for i in range(5):
    num = int(input("Digite um número: "))
    lista.append(num)  # Adiciona o número digitado à lista
x = max(lista)  # Encontra o maior número na lista
print(f"O maior número entre os numeros {lista} é: {x}")  # Imprime o maior número encontrado