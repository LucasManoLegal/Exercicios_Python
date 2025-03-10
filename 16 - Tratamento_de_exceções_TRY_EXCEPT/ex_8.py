# 8. Crie uma função contar_caracteres(texto, caractere) que conta quantas vezes um caractere aparece em um texto. Se texto não for uma string, exiba um erro.

def contar_caracteres(texto, caractere):
    try:
        contador = 0
        # Solicita ao usuário que insira um texto e um caractere.
        texto = input("Digite um texto: ")
        caractere = input("Agora digite um caractere: ")
        # Itera sobre o texto e conta quantas vezes o caractere aparece.
        for i in texto:
            if i == caractere:
                contador += 1
        # Imprime o resultado da contagem.
        print(f"O caractere '{caractere}' aparece {contador} vezes.")
    except ValueError:
        # Se ocorrer ValueError, exibe uma mensagem de erro.
        print("Erro: valor inválido.")

# Inicializa as variáveis texto e caractere.
texto = ""
caractere = ""

# Chama a função contar_caracteres.
contar_caracteres(texto, caractere)