# 5. Crie uma função soma_lista(numeros) que recebe uma lista de números e retorna a soma. Se a lista contiver valores inválidos, capture a exceção e exiba uma 
# mensagem de erro.

lista = []

def soma_lista(numeros, lista = []):
    try:
        while numeros != 0:
            numeros = int(input("Digite um número ou digite 0 para sair: "))
            lista.append(numeros)
        return sum(lista)
    except ValueError:
        return "Erro: O valor inserido não é válido."
    
print(soma_lista(lista))
