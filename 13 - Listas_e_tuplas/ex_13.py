#13. Criar uma lista de números e imprimir apenas os números ímpares.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

impares = []

for i in lista:
    if not i % 2 == 0:
        impares.append(i)

print(f"Os números ímpares da lista são: {impares}.")