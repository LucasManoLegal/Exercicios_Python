# 6. Crie uma função multiplicar(a, b) que retorna o produto de a e b. Se os valores não forem números, capture a exceção e exiba uma mensagem de erro.

def multiplicar(a = 0, b = 0):
    try:
        a = int(input("Digite o primero número: "))
        b = int(input("Digite o segundo número: "))
        resultado = a * b
        print(f"O resultado é {resultado}.")
    except ValueError:
        print("Erro: Os valores precisam ser números inteiros.")



multiplicar()
