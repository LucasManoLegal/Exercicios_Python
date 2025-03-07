# 15. Faça um programa que receba a idade de 15 pessoas e que calcule e mostre:
# a) A quantidade de pessoas em cada faixa etária;
# b) A porcentagem de pessoas na primeira e na última faixa etária, com relação ao total de pessoas:
# - Até 15 anos
# - De 16 a 30 anos
# - De 31 a 45 anos
# - De 46 a 60 anos
# - Acima de 61 anos

faixaEtaria1 = 0
faixaEtaria2 = 0
faixaEtaria3 = 0
faixaEtaria4 = 0
faixaEtaria5 = 0

for i in range(15):  # Loop para coletar a idade de 15 pessoas
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    if idade >= 1 and idade <= 15:  # Verifica se a idade está na primeira faixa etária
        faixaEtaria1 += 1  # Incrementa o contador da primeira faixa etária
    if idade >= 16 and idade <= 30:  # Verifica se a idade está na segunda faixa etária
        faixaEtaria2 += 1  # Incrementa o contador da segunda faixa etária
    if idade >= 31 and idade <= 45:  # Verifica se a idade está na terceira faixa etária
        faixaEtaria3 += 1  # Incrementa o contador da terceira faixa etária
    if idade >= 46 and idade <= 60:  # Verifica se a idade está na quarta faixa etária
        faixaEtaria4 += 1  # Incrementa o contador da quarta faixa etária
    if idade >= 61:  # Verifica se a idade está na quinta faixa etária
        faixaEtaria5 += 1  # Incrementa o contador da quinta faixa etária
percentualFaixaEtaria1 = (faixaEtaria1 / 100) * 15 # Cálculo incorreto da porcentagem
percentualFaixaEtaria5 = (faixaEtaria5 / 100) * 15 # Cálculo incorreto da porcentagem

print(f"Até 15 anos: {faixaEtaria1} pessoa(s)")  # Imprime a quantidade de pessoas na primeira faixa etária
print(f"De 16 a 30 anos: {faixaEtaria2} pessoa(s)")  # Imprime a quantidade de pessoas na segunda faixa etária
print(f"De 31 a 45 anos: {faixaEtaria3} pessoa(s)")  # Imprime a quantidade de pessoas na terceira faixa etária
print(f"De 46 a 60 anos: {faixaEtaria4} pessoa(s)")  # Imprime a quantidade de pessoas na quarta faixa etária
print(f"Acima de 61 anos: {faixaEtaria5} pessoa(s)")  # Imprime a quantidade de pessoas na quinta faixa etária
print(f"Porcentagem de pessoas na primeira faixa etária: {percentualFaixaEtaria1 * 100}")  # Imprime a porcentagem de pessoas na primeira faixa etária
print(f"Porcentagem de pessoas na ultima faixa etária: {percentualFaixaEtaria5 * 100}")  # Imprime a porcentagem de pessoas na quinta faixa etária
