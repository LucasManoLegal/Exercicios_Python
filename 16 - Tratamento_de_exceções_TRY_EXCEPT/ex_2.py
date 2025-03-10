# 2. Crie uma função ler_inteiro() que solicita ao usuário um número inteiro. Se o usuário inserir um valor inválido (não inteiro), exiba uma mensagem e peça a entrada
# novamente até que um número válido seja fornecido.

def ler_inteiro():
    while True:  
        try:
            # Solicita ao usuário que insira um número inteiro.
            numero = int(input("Digite um número inteiro: "))  
            print("Número OK!")  
            return numero
        except ValueError:  
            # Se ocorrer ValueError, exibe uma mensagem de erro.
            print("Erro. O número não é um inteiro. Tente novamente.")  

# Chama a função ler_inteiro e imprime o número inserido.
print(f'O número inserido foi:', ler_inteiro())





