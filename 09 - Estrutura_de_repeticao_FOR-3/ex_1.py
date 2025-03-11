# 1. Faça um programa que leia 5 números e informe o maior número.

# Inicializa a variável para armazenar o maior número
maior_numero = None

# Lê 5 números e verifica qual é o maior
for i in range(5):
    num = int(input("Digite um número: "))
    
    # Se for o primeiro número, define como o maior
    if maior_numero is None or num > maior_numero:
        maior_numero = num

# Imprime o maior número encontrado
print(f"O maior número digitado é: {maior_numero}")
