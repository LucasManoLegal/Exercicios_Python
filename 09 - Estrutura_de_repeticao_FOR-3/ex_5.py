# 5. Faça um programa que receba um número e usando laços de repetição calcule e mostre a tabuada desse número.

num = int(input("Digite um número: "))
print(f"Tabuada no número {num}")
for i in range(1, 11):  # Loop para multiplicar o número digitado por 1 a 10
    print(f"{num} x {i} = {num*i}")  # Imprime a tabuada