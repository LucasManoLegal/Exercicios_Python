# 7. Crie uma função pegar_elemento(lista, indice) que retorna o elemento de uma lista na posição indice. Se o índice não existir, trate o erro.

def pegar_elemento(lista, indice):
    try:
        return f"O item no índice digitado é: {lista[indice]}"
    except IndexError:
        return "Erro: O índice digitado não corresponde à lista."
    

lista = [1, 2, 3, 4, 5]
indice = int(input("Digite o índice do item desejado: "))  

print(pegar_elemento(lista, indice))

