# 2. Escreva um programa que leia um número inteiro positivo e determine se ele é um
# palíndromo (ou seja, se lido de trás para frente continua igual).
# Leitura do número inteiro positivo


palavra = input("Digite uma palavra: ")
palavraInvertida = palavra[::-1]

    # Compara a palavra original com sua versão invertida.
if palavra == palavraInvertida:
    # Se forem iguais, retorna a string "A palavra é um palíndromo.".
    print("A palavra é um palíndromo.")
else:
    # Se não forem iguais, retorna a string "A palavra não é um palíndromo.".
    print("A palavra não é um palíndromo.")


