# 5: Crie uma função chamada tabuada que recebe um número e imprime sua tabuada do 1 ao 10.

# Solicita ao usuário que digite um número e converte a entrada para um inteiro.
num = int(input("Digite um número e veja sua tabuada: "))

# Define uma função chamada 'tabuada' que recebe um número como argumento.
def tabuada(num):
    # Itera sobre os números de 1 a 10.
    for i in range(1, 11):
        # Imprime a linha da tabuada para o número atual.
        print(f"{num} x {i} = {num*i}")

# Chama a função 'tabuada' com o número fornecido pelo usuário.
tabuada(num)