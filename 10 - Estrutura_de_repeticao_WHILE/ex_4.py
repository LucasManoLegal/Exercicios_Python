senhaCorreta = "1234"
senha = input("Digite sua senha: ")

while senha != senhaCorreta: # enquanto a senha não for "1234":
    print("Senha incorreta. Tente novamente.")
    senha = input("Digite sua senha: ") # Pede a senha novamente, e assim o loop contiua
print("Senha OK!") # Quando a senha for "1234", o loop é encerrado, mostrando assim uma mensagem de sucesso.