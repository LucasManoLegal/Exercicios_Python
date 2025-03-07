# 3. Crie uma função que recebe uma lista de números e retorna a quantidade de números que são múltiplos de 3.

lista = [1, 6, 4, 9, 7, 12, 8, 11, 15]

def multiplosDe3(lista):
    contador = 0  # Inicializa o contador dentro da função
    for numero in lista:  # Itera sobre os números da lista
        if numero % 3 == 0:  # Verifica se o número é múltiplo de 3
            contador += 1  # Incrementa o contador se for múltiplo de 3
    return contador

print("Na lista,", multiplosDe3(lista), "números são múltiplos de 3.")  # Imprime o resultado