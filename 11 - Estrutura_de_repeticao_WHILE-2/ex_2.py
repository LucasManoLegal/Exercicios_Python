# 2. Solicite ao usuário que insira uma senha e continue pedindo até que ele insira a senha correta definida previamente.

senha = input("Digite uma senha: ")
confirmar = input("Digite novamente a senha: ")

while senha != confirmar:
    print("Senha incorreta.")
    senha = input("Digite uma senha: ") # Inicia novamente o loop
    confirmar = input("Digite novamente a senha: ")
print("Obrigado!")