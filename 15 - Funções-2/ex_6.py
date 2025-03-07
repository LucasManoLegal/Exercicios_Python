# 6. Crie uma função que recebe uma lista de palavras e retorna a palavra com mais letras.

lista = ['banana', 'maçã', 'pêra', 'abacaxi']

def maiorPalavra(maior_palavra = max(lista, key=len)):
    return maior_palavra # Retorna a palavra com mais letras.

print("A palavra da lista com mais letras é:", maiorPalavra()) # Imprime a palavra com mais letras.
