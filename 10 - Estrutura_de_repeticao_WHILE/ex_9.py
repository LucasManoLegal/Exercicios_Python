# 9. Contar quantos números pares o usuário digitar. O programa deve contar quantos números pares o usuário inseriu. O usuário para digitando -1. 
par = 0
qtdNum = 0
num = int(input("Digite um número, ou digite '-1' para sair: "))

while num != -1:
    qtdNum += 1 # de qualquer forma, quando um número válido for digitado, o contador 
    if num % 2 == 0:
        par += 1 # aqui o contador dos pares é incrementado APENAS quando o número for par.
    num = int(input("Digite um número: ")) # inicia o loop novamente.
print(f"Dos {qtdNum} números que você digitou, {par} são ímpares.") # quando o input for igual a '-1' o loop se encerra.