# 6. Solicite ao usuário uma nota entre 0 e 10. Caso o valor seja inválido, peça novamente até que o usuário informe um valor válido.

nota = int(input("Digite uma nota de 0 a 10: "))

while nota < 0 or nota > 10:
    print("Nota inválida. Digite novamente.") # se o número não se enquadrar entre u a 10, o programa vai pedir para que o usuário digite novamente
    nota = int(input("Digite uma nota de 0 a 10: "))
print("Nota OK!") # quando o usuário digitar uma nota válida, o loop se encerra.
