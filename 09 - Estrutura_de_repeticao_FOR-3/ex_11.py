# 11. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o
# número de votos de cada candidato.

a = 0
b = 0
c = 0

numEleitores = int(input("Digite o número total de eleitores: "))
for i in range(numEleitores):  # Loop para coletar o voto de cada eleitor
    voto = input("Digite 'A' para votar no candidato A, 'B' para votar no candidato B e 'C' para votar no candidato C: ").upper().strip()  # Coleta o voto e converte para maiúsculas, removendo espaços em branco
    if voto == "A":  # Verifica se o voto é para o candidato A
        a += 1  # Incrementa o contador de votos para o candidato A
    elif voto == "B":  # Verifica se o voto é para o candidato B
        b += 1  # Incrementa o contador de votos para o candidato B
    elif voto == "C":  # Verifica se o voto é para o candidato C
        c += 1  # Incrementa o contador de votos para o candidato C
print(f"Candidato A: {a} votos.")  # Imprime o número de votos para o candidato A
print(f"Candidato B: {b} votos.")  # Imprime o número de votos para o candidato B
print(f"Candidato C: {c} votos.")  # Imprime o número de votos para o candidato C

# Este programa simula uma eleição com três candidatos. Ele coleta o voto de cada eleitor e, no final, mostra o número de votos para cada candidato.