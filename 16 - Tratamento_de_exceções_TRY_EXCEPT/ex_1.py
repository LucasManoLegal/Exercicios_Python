# 1. Crie uma função chamada calculadora que receba três parâmetros: dois números e uma operação (+, -, *, /). A função deve retornar o resultado da operação,  mas 
# precisa tratar as seguintes exceções:
# - Divisão por zero (ZeroDivisionError)
# - Tipo de dado inválido (ValueError)

def calculadora(num1 = 0, operacao = "0", num2 = 0):
    try:
        # Solicita ao usuário que insira um número, a operação e outro número.
        num1 = int(input("Digite um número: "))
        operacao = input("Digite a operação: ")
        num2 = int(input("Digite outro número: "))

        # Realiza a operação com base na entrada do usuário.
        if operacao == "+":
            return num1 + num2
        if operacao == "-":
            return num1 - num2
        if operacao == "*":
            return num1 * num2
        if operacao == "/":
            return num1 / num2
        else:
            return "Operador fora das opções disponíveis."
    except ZeroDivisionError:
        # Se ocorrer ZeroDivisionError, retorna uma mensagem de erro.
        return "Erro: Divisão por 0."
    except ValueError:
        # Se ocorrer ValueError, retorna uma mensagem de erro.
        return "Erro: Valor inválido."
    
# Chama a função calculadora e imprime o resultado (ou a mensagem de erro).
print(calculadora())