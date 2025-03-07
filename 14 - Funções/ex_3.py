# 3: Crie uma função chamada media_lista que recebe uma lista de números e retorna a média deles.
# Define uma lista de números.

lista = [7, 8, 9, 10]

# Define uma função chamada 'media_lista' que recebe uma lista como argumento.
def media_lista(lista):
    # Calcula a média da lista somando todos os elementos e dividindo pelo número de elementos.
    return sum(lista) / len(lista)

# Chama a função 'media_lista' com a lista definida e imprime o resultado.
print(media_lista(lista))