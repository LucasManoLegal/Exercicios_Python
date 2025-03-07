# 12. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

contadorPares = 0
contadorImpares = 0

for i in range(10):  # Loop para coletar 10 números
    num = int(input("Digite um número: "))
    if num % 2 == 0:  # Verifica se o número é par (resto da divisão por 2 é 0)
        contadorPares += 1  # Incrementa o contador de números pares
    else:
        contadorImpares += 1  # Incrementa o contador de números ímpares
print(f"Dos 10 números que você digitou, {contadorPares} são pares e {contadorImpares} são ímpares.")  # Imprime a quantidade de números pares e ímpares