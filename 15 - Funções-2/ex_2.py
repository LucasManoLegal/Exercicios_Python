# 2. Crie uma função que recebe uma lista de números e retorn a quantidade de números positivos.

lista = [-3, 1, 5, -9, 7, -8, -10, 4, 7, -13]

def contadorPositivos(lista):
    contador = 0  # Inicializa o contador dentro da função
    for numero in lista:  # Itera sobre os números da lista
        if numero > 0:  # Verifica se o número é positivo
            contador += 1  # Incrementa o contador se for positivo
    return contador

positivos = contadorPositivos(lista)  # Chama a função e armazena o resultado
print(f"Na lista, existem {positivos} números positivos.")  # Imprime o resultado