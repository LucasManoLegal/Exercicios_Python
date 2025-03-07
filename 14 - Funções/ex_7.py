# 7: Crie uma função que receba uma lista de números e retorne o maior número dessa lista.

# Define uma lista de números.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Define uma função chamada 'maiorNumero' que recebe uma lista como argumento.
def maiorNumero(lista):
    # Usa a função 'max' para encontrar o maior número na lista e retorna esse número.
    return max(lista)

# Chama a função 'maiorNumero' com a lista definida e imprime o resultado.
print("O maior número da lista é:", maiorNumero(lista))

