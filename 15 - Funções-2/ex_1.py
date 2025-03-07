# 1. Crie uma função que recebe duas palavras e retorna True se forem anagramas uma da outra.

palavra1 = input("Digite uma palavra: ")
palavra2 = input("Digite outra palavra: ")

print(f"As palavras {palavra1} e {palavra2} são anagramas uma da outra?")

def anagrama(palavra1, palavra2):
    # Ordena as letras das duas palavras e compara se elas são iguais
    if sorted(palavra1) == sorted(palavra2):
        return True  # Se forem iguais, são anagramas
    else:
        return False  # Se não forem iguais, não são anagramas

# Chama a função e imprime o resultado
print(anagrama(palavra1, palavra2))
