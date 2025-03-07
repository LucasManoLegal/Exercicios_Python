# 3. Faça um programa que verifique e mostre os números entre 1.000 e 2.000 que, quando divididos por 11 produzam resto igual a 2.

for i in range(1000, 2001):  # Loop para iterar sobre os números de 1000 a 2000
    if i % 11 == 2:  # Verifica se o resto da divisão por 11 é igual a 2
        print(i)  # Imprime o número se a condição for verdadeira
