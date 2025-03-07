# 4: Crie uma função que calcule o fatorial de um número.

# Solicita ao usuário que digite um número e converte a entrada para um inteiro.
num = int(input("Digite número e veja o resultado de seu fatorial: "))

# Define uma função chamada 'fatorial' que calcula o fatorial de um número.
def fatorial(num, contador = 1):
    # Itera sobre um range do tamanho do número fornecido.
    for i in range(num):
        # Multiplica o contador pelo valor atual de 'i' mais 1.
        contador *= (i+1)
    
    # Retorna o valor final do contador, que é o fatorial do número.
    return contador

# Chama a função 'fatorial' com o número fornecido pelo usuário e imprime o resultado.
print(fatorial(num))
