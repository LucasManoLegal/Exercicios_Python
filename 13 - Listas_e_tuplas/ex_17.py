# 17. Criar uma lista de 5 números e multiplicar cada número por 3.

lista = [1, 2, 3, 4, 5]
index = 0

print(lista)

for num in lista:
    num *= 3
    lista[index] = num
    index += 1

print(lista)
