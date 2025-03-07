# 4. Crie uma função que recebe uma lista de palavras e junta tudo em uma única frase.

lista = ['Hello ', 'World!']

def juntarPalavras(lista):
    return "".join(lista)  # Usa o método join para concatenar as strings

print(juntarPalavras(lista))  # Imprime o resultado