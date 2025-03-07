# 7. Criar uma lista de strings e verificar quantas vezes uma palavra específica aparece.

lista = ["Charlinho", "Joselito", "Boça", "Joselito", "Hermes", "Joselito", "Renato"]
contador = 0

for i in lista:
    if i == "Joselito":
        contador += 1
print(f"A palavra Joselito aparece {contador} vezes.")