# 5. Solicite ao usuário números indefinidamente. O programa deve parar quando o usuário digitar um número igual ao anterior. Em seguida, exiba quantos números foram inseridos.

# Inicializa o contador de números inseridos
contador = 0

# Solicita o primeiro número
num = int(input("Digite um número: "))
contador += 1  # Contador começa com 1, já que o primeiro número foi inserido

# Solicita o próximo número
numAnterior = num  # Armazena o primeiro número inserido
while True:
    num = int(input("Digite um número: "))
    contador += 1  # Incrementa o contador

    # Verifica se o número inserido é igual ao anterior
    if num == numAnterior:
        print(f"Programa encerrado. Você digitou {contador} números.")
        break  # Encerra o loop quando o número for igual ao anterior

    # Atualiza o número anterior
    numAnterior = num


    
