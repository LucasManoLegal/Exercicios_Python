# 3. Peça ao usuário que insira notas (valores numéricos). A entrada deve continuar até que o usuário digite -1. Em seguida, exiba a média das notas.

soma = 0
media = 0
contador = 0
nota = int(input("Digite uma nota: (Digite -1 para sair) "))

while nota != -1:
    soma += nota # incrementa os valores digitados a variável soma
    contador += 1 # o contador é útil para sabermos a quantidade dos números para assim dividirmos pela soma e resultar na média.
    nota = int(input("Digite uma nota: (Digite -1 para sair) ")) # Inicia o loop novamente.
media = soma / contador
print(f"A media dos números é {media}.")

