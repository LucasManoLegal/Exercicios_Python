# 9: Crie uma função que conte quantas vogais existem em uma string fornecida.

# Solicita ao usuário que digite uma palavra.
palavra = input("Digite uma palavra e veja quantas vogais existem: ")

# Define uma função chamada 'contarVogais' que recebe uma palavra como argumento.
def contarVogais(palavra, contadorVogais = 0, vogais = 'aeiou'):
    # Itera sobre cada caractere na palavra.
    for i in palavra:
        # Verifica se o caractere atual está na string de vogais 'aeiou'.
        if i in vogais:
            # Se for uma vogal, incrementa o contador de vogais.
            contadorVogais += 1
    # Retorna o número total de vogais encontradas na palavra.
    return contadorVogais

# Chama a função 'contarVogais' com a palavra fornecida pelo usuário e imprime o resultado.
print(f"Na palavra {palavra}, existem", contarVogais(palavra), 'vogais.')