# 4. Verificar se um número específico está presente na lista.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num = int(input("Digite um número: "))

if num in lista:
    print("O número está na lista.")
else:
    print("O número não está na lista")