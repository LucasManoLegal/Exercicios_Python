# 8: Crie uma função que receba uma lista de notas e retorne a média das notas.

# Define uma lista de notas.
notas = [7, 8, 9, 10]

# Define uma função chamada 'mediaNotas' que recebe uma lista de notas como argumento.
def mediaNotas(notas):
    # Calcula a média das notas somando todas as notas e dividindo pelo número de notas.
    return sum(notas) / len(notas)

# Chama a função 'mediaNotas' com a lista de notas definida e imprime o resultado.
print("A média das notas é:", mediaNotas(notas))