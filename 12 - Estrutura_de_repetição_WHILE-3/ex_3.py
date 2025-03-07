# 4. Escreva um programa que leia um número inteiro positivo e determine se ele é um número perfeito. Um número perfeito é aquele cuja soma dos seus divisores próprios
# (excluindo ele mesmo) é igual ao próprio número.

num = int(input("Digite um número: "))
divisor = 1 # O divisor começa em 1 pois o dividir por 0 gera uma indeterminação.
soma = 0
while divisor < num: 
    if num % divisor == 0: # O programa pega os divisores e verifica se, ao dividir pelo número digitado, não sobra resto, o que significa que ele é um divisor válido.
        soma += divisor # Se o divisor for válido, ele é incrementado a variável soma para mais uma verficação.
    divisor += 1 # Adiciona 1 ao divisor e o loop é reiniciado com seu valor alterado.
if soma == num: # Se a soma dos divisores for igual ao número digitado, significa que o número é perfeito.
    print(f"{num} é um número perfeito.")
else:
    print(f"{num} não é um número perfeito.")