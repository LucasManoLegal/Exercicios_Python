# 7. Crie uma função pegar_elemento(lista, indice) que retorna o elemento de uma lista na posição indice. Se o índice não existir, trate o erro.

def pegar_elemento(lista, indice):
    try:
        # Tenta acessar o elemento da lista no índice especificado.
        return f"O item no índice digitado é: {lista[indice]}"
    except IndexError:
        # Se ocorrer IndexError, retorna uma mensagem de erro.
        return "Erro: O índice digitado não corresponde à lista."
    

# Define uma lista de exemplo.
lista = [1, 2, 3, 4, 5]
# Solicita ao usuário que insira o índice do item desejado.
indice = int(input("Digite o índice do item desejado: "))  

# Chama a função pegar_elemento e imprime o resultado (ou a mensagem de erro).
print(pegar_elemento(lista, indice))

