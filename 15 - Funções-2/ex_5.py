# 5. Crie uma função que recebe uma lista de números e substitui os números negativos por zero.

lista = [-3, 1, 5, -9, 7, -8, -10, 4, 7, -13]

def substituirNegativos(lista):
    for i in range(len(lista)):  # Usando índice para modificar diretamente a lista
        if lista[i] < 0:  # Verifica se o número na lista é negativo
            lista[i] = 0  # Substitui o número negativo por zero
    print(lista)

substituirNegativos(lista)  # Agora imprime a lista modificada




