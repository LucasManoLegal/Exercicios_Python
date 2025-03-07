# 8. Encontrando o maior número inserido pelo usuário. Peça números ao usuário e, ao digitar 0, exiba o maior número inserido.
lista = []
num = int(input("Digite um número: "))

while num != 0:
    lista.append(num) # Adiciona o número digitado à lista
    num = int(input("Digite um número: ")) # inicia o loop novamente
x = max(lista) # x é o maior valor dentro da lista

print(f"O maior número é {x}")  # Imprime o maior número encontrado
