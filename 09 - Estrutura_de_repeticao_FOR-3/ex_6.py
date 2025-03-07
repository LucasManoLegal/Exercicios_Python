# 6. Faça um programa que mostre as tabuadas dos números de 1 a 10 usando laços de repetição.

for i in range(1, 11):  # Loop externo para os números de 1 a 10 (tabuada de cada número)
    print(f"Tabuada do {i}:")
    for j in range(1, 11):  # Loop interno para multiplicar o número atual (i) por 1 a 10
        print(f"{i} x {j} = {i * j}")