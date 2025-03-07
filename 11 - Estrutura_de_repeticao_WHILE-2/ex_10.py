# 10. Implemente um sistema de votação onde o usuário pode votar em candidatos (1 a 4), nulo (5) ou branco (6). O programa deve exibir o total de votos de cada tipo e a porcentagem de votos nulos e brancos. A entrada 0 encerra a votação.

voto = int(input('''Digite de 1 a 6 para votar OU digite 0 para encerrar a votação:
1 - Candidato A    
2 - Candidato B 
3 - Candidato C
4 - Candidato D  
5 - Voto nulo
6 - Voto em branco              
'''))
candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulo = 0
branco = 0
total = 0

while True:
    if voto == 1:
        candidato1 += 1
        total += 1
    elif voto == 2:
        candidato2 += 1
        total += 1
    elif voto == 3:
        candidato3 += 1
        total += 1
    elif voto == 4:
        candidato4 += 1
        total += 1
    elif voto == 5:
        nulo += 1
        total += 1
    elif voto == 6:
        branco += 1
        total += 1
    elif voto == 0:
        porcentagemNulo = (nulo / 100) * total
        porcentagemBranco = (branco / 100) * total

        print("Votação encerrada.")
        print(f"Candidato 1: {candidato1} votos.")
        print(f"Candidato 2: {candidato2} votos.")
        print(f"Candidato 3: {candidato3} votos.")
        print(f"Candidato 4: {candidato4} votos.")
        print(f"Nulo: {nulo} votos.")
        print(f"{porcentagemNulo * 100}% de votos nulos em relação ao total.")
        print(f"Branco: {branco} votos.")
        print(f"{porcentagemBranco * 100}% de votos brancos em relação ao total.")
        break
    else:
        print("Voto inválido.")
        voto = int(input('''Digite de 1 a 6 para votar OU digite 0 para encerrar a votação:
1 - Candidato A    
2 - Candidato B 
3 - Candidato C
4 - Candidato D  
5 - Voto nulo
6 - Voto em branco              
'''))
    voto = int(input('''Digite de 1 a 6 para votar OU digite 0 para encerrar a votação:
1 - Candidato A    
2 - Candidato B 
3 - Candidato C
4 - Candidato D  
5 - Voto nulo
6 - Voto em branco              
'''))


