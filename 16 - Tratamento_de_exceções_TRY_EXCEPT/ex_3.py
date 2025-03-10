# 3. Crie uma função calcular_media(numeros) que recebe uma lista de números e retorna a média. Se a lista estiver vazia, a função deve tratar a exceção e exibir uma
# mensagem adequada.

def calcular_media(numeros):
    while True:
        try:
            if numeros != 0:
                # Solicita ao usuário que insira números até digitar 0.
                numeros = int(input("Digite números: (Digite 0 para sair)"))
                if numeros == 0:
                    return "Programa encerrado."
                lista.append(numeros)
                numeros = int(input("Digite números: (Digite 0 para sair)"))
            else:
                # Calcula a média dos números na lista.
                media = sum(lista) / len(lista)
                return f"Média: {media}"
        except ValueError:
            # Se ocorrer ValueError, retorna uma mensagem de erro.
            return "Erro. Lista vazia / valor inválido."
        
# Inicializa uma lista vazia e uma variável para controlar o loop.
lista = []
numeros = 1
# Chama a função calcular_media e imprime o resultado (ou a mensagem de erro).
print(calcular_media(numeros))





             



    
