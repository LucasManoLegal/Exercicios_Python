# 4. Solicite ao usuário que insira números. O programa deve continuar até que um número negativo seja inserido. No final, exiba o maior número informado.

# Inicializa a variável para armazenar o maior número
maiorNumero = None

# Lê números até o usuário digitar um número negativo
num = int(input("Digite um número (Digite um número negativo para sair): "))

while num >= 0:
    # Se for o primeiro número ou um número maior que o atual maior, atualiza o maior
    if maiorNumero is None or num > maiorNumero:
        maiorNumero = num
        
    # Pede o próximo número
    num = int(input("Digite um número: "))

# Exibe o maior número encontrado
print(f"O maior número digitado foi {maiorNumero}")
