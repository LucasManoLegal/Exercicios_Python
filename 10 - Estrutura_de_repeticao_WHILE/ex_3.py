# 3. Somar números até o usuário digitar 0. Peça números ao usuário e some-os até que ele digite 0.

num = int(input("Digite um número, digite 0 para sair: "))
soma = 0

while num != 0: # Enquanto o número for tudo, MENOS 0:
    soma += num # Incrementa o valor inputado á variável soma
    num = int(input("Digite outro número, digite 0 para sair: ")) # Pede novamente o número, e assim o loop se inicia novamente.
print(f"A soma dos números é {soma}.") # se o usuário digitar 0, o loop se encerra.
