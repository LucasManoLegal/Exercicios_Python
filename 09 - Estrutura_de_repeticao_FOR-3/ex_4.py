# 4. Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0

for i in range(5):  # Loop para ler 5 números do usuário
    num = int(input("Digite um número: "))
    soma += num  # Adiciona o número digitado à variável soma
media = soma / 5  # Calcula a média dividindo a soma por 5
print(f"A média dos números é: {media}")  # Imprime a média