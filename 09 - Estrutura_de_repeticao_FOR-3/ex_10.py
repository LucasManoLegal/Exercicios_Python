# 10. Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
# e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

somaIdades = 0
contador = 0

numPessoas = int(input("Digite o número de pessoas na turma: "))
for i in range(numPessoas):  # Loop para coletar a idade de cada pessoa
    idade = int(input("Digite a idade de cada pessoa na turma: "))
    contador += 1  # Incrementa o contador de pessoas
    somaIdades += idade  # Adiciona a idade à soma total
media = somaIdades / contador  # Calcula a média das idades
if media >= 0 and media <= 25:  # Verifica se a média está entre 0 e 25 (inclusive)
    print("A turma é jovem.")
elif media >= 26 and media <= 60:  # Verifica se a média está entre 26 e 60 (inclusive)
    print("A turma é adulta.")
elif media > 60:  # Verifica se a média é maior que 60
    print("A turma é idosa.")
