numSecreto = 7
num = int(input("Tente adivinhar o número secreto. Ele está entre 1 e 10: "))

while num != 7:
    print("Número incorreto.")
    num = int(input("Tente adivinhar o número secreto. Ele está entre 1 e 10: ")) # Pede mais uma tentavita ao usuário, inciando o loop mais uma vez.
print("Parabéns! você adivinhou o número secreto!") # quando o número digitado for 7, o loop se encerra.

