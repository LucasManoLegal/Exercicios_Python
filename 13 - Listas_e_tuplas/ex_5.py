# 5. Criar uma lista de números e imprimir apenas os números pares.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = []

for i in lista:
    if i % 2 == 0:
        pares.append(i)

print(f"Os números pares da lista são: {pares}.")