# 8. Encontrando o maior número inserido pelo usuário. Peça números ao usuário e, ao digitar 0, exiba o maior número inserido.

# Inicializa a variável para armazenar o maior número
maior_numero = None

# Lê números até o usuário digitar 0
while True:
    num = int(input("Digite um número (ou 0 para sair): "))
    
    if num == 0:
        break
    
    # Se for o primeiro número ou um número maior que o atual maior, atualiza o maior
    if maior_numero is None or num > maior_numero:
        maior_numero = num

# Exibe o maior número inserido
print(f"O maior número é {maior_numero}")

