# 3. Escreva um programa que leia um número inteiro e conte quantos dígitos ele tem.

num = input("Digite um número: ")
contador = 0

while contador < len(num): # Adiciona 1 ao contador de dígitos até que o contador se iguale a quantidade de caracteres.
    contador += 1

print(f"O número {num} tem {contador} dígitos.")

