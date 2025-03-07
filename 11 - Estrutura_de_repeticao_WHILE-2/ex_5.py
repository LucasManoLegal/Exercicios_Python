# 5. Solicite ao usuário números indefinidamente. O programa deve parar quando o usuário digitar um número igual ao anterior. Em seguida, exiba quantos números foram inseridos.

lista = []
contador = 0

# Solicita o primeiro número
num = int(input("Digite um número: "))
lista.append(num)  # Adiciona o primeiro número na lista
contador += 1  # Contador começa com 1, já que o primeiro número foi inserido

while True:
    # Solicita o próximo número
    numNovo = int(input("Digite um número: "))
    
    # Verifica se o número inserido é igual ao anterior
    if numNovo == lista[-1]:
        print(f"Programa encerrado. Você digitou {contador} números.")
        break  # Encerra o loop quando o número for igual ao anterior
    
    # Se o número não for igual, adiciona à lista e incrementa o contador
    lista.append(numNovo)
    contador += 1

    
