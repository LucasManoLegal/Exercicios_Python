# Define uma função chamada divisao_segura que realiza a divisão de dois números.

def divisao_segura():
    try:
        # Solicita ao usuário que insira dois números.
        num1 = int(input("Digite um numero: "))
        num2 = int(input("Digite outro numero: "))

        # Tenta realizar a divisão e retorna o resultado.
        return num1 / num2
    except ZeroDivisionError:
        # Se ocorrer ZeroDivisionError, retorna uma mensagem de erro.
        return "Erro: Divisão por zero não permitida!"

# Chama a função divisao_segura e imprime o resultado (ou a mensagem de erro).
print(divisao_segura())