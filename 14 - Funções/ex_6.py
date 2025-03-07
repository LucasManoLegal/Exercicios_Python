# 6: Crie uma função que receba uma string e retorne True se ela for um palíndromo (uma palavra ou frase que se lê da mesma forma de trás para frente) e False caso contrário.

# Solicita ao usuário que digite uma palavra.
palavra = input("Digite uma palavra: ")

# Define uma função chamada 'palindromo' que recebe uma palavra como argumento.
def palindromo(palavra, palavraInvertida = palavra[::-1]):
    # Compara a palavra original com sua versão invertida.
    if palavra == palavraInvertida:
        # Se forem iguais, retorna a string "A palavra é um palíndromo.".
        return "A palavra é um palíndromo."
    else:
        # Se não forem iguais, retorna a string "A palavra não é um palíndromo.".
        return "A palavra não é um palíndromo."

# Chama a função 'palindromo' com a palavra fornecida pelo usuário e imprime o resultado.
print(palindromo(palavra))
