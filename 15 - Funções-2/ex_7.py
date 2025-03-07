# 7. Crie uma função que recebe uma lista de números e retorna a soma apenas dos números pares.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def somaPares(lista):
    soma = 0  # Inicializa a soma com 0
    for numero in lista:  # Itera sobre os números da lista
        if numero % 2 == 0:  # Verifica se o número é par
            soma += numero  # Adiciona o número par à soma
    return soma

print("A soma dos números pares da lista é", somaPares(lista))  # Imprime o resultado