# 13. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
nota = 0

for i in range(10): #Permite até 10 tentativas
    nota = int(input("Digite uma nota: "))
    if nota < 0 or nota > 10:  # Verifica se a nota está fora do intervalo válido (0 a 10)
        print("Valor inválido. Digite novamente.")
    else:
        print("Nota OK!")
        break # Sai do loop se a nota for válida


        
