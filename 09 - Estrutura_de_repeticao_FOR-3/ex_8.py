# 8. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
num = int(input("Digite um número: "))

if num < 2:  # Números menores que 2 não são primos
    print("Não é primo.")
else:
    for i in range(2, num):  # Loop para verificar se o número é divisível por algum número entre 2 e ele mesmo - 1
        if num % i == 0:  # Se for divisível, não é primo
            print("Não é primo.")
            break  # Sai do loop se encontrar um divisor
    else:
        print("É primo.")  # Se o loop completar sem encontrar um divisor, é primo