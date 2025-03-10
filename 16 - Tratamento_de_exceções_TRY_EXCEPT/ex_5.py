# 5. Crie uma função soma_lista(numeros) que recebe uma lista de números e retorna a soma. Se a lista contiver valores inválidos, capture a exceção e exiba uma 
# mensagem de erro.

lista = []

def soma_lista(numeros):
    try:
        # Solicita ao usuário que insira números até digitar 0.
        while numeros != 0:
            numeros = int(input("Digite um número ou digite 0 para sair: "))
            lista.append(numeros)
        # Calcula a soma dos números na lista.
        return sum(lista)
    except ValueError:
        # Se ocorrer ValueError, retorna uma mensagem de erro.
        return "Erro: O valor inserido não é válido."
    
# Chama a função soma_lista e imprime o resultado (ou a mensagem de erro).
print(soma_lista(lista))
