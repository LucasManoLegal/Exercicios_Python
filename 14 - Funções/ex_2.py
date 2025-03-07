# 2: Crie uma função que receba um número e retorne "Par" se o número for par ou "Ímpar" se o número for ímpar.

# Solicita ao usuário que digite um número e converte a entrada para um inteiro.
num = int(input("Digite um número e veja se ele é par ou ímpar: "))

# Define uma função chamada 'parImpar' que recebe um número como argumento.
def parImpar(num):
    # Verifica se o número é divisível por 2 (ou seja, se é par).
    if num % 2 == 0:
        # Se for par, retorna a string "par".
        return "par"
    else:
        # Se não for par (ou seja, se for ímpar), retorna a string "ímpar".
        return "ímpar"
# Chama a função 'parImpar' com o número fornecido pelo usuário e imprime o resultado.
print("O numero é", parImpar(num))