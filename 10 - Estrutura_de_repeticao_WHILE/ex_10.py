# 10. Apenas aceitar números positivos. O programa deve continuar pedindo um número até o usuário digitar um número negativo.

num = int(input("Digite um número. OBS: Ele deve ser positivo: "))

while num >= 0: # Enquanto o número inputado for POSITIVO:
    num = int(input("Digite um número. OBS: Ele deve ser positivo: ")) # Inicia o loop novamente.
print("Número inválido.") # O valor inputado é NEGATIVO, encerrando assim o loop.