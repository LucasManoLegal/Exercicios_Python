# 16. Criar uma lista de nomes e exibir apenas os nomes que começam com a letra &quot;A&quot;.

nomes = ['Charlinho', 'Adriano', 'Joselito', 'Andréia', 'Boça', 'Ariel', 'Hermes', 'Ana', 'Renato']
inicialA = []

for i in nomes:
    if i.startswith('A'):
        inicialA.append(i)
        
print(inicialA)