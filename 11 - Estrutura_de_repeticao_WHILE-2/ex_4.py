# 4. Solicite ao usuário que insira números. O programa deve continuar até que um número negativo seja inserido. No final, exiba o maior número informado.

lista = []
num = int(input("Digite um número: (Digite um número negativo para sair)."))

while num >= 0:
    lista.append(num) # Adiciona o valor inputado a lista.
    num = int(input("Digite um número: "))

x = max(lista) # Retorna o maior valor da lista.

print(f"Dentre os números {lista}, {x} é o maior número.")