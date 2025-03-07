# 1. Crie uma função chamada calculadora que receba três parâmetros: dois números e uma operação (+, -, *, /). A função deve retornar o resultado da operação,  mas 
# precisa tratar as seguintes exceções:
# - Divisão por zero (ZeroDivisionError)
# - Tipo de dado inválido (ValueError)

def calculadora(num1 = 0, operacao = "0", num2 = 0):
    try:
        num1 = int(input("Digite um número: "))
        operacao = input("Digite a operação: ")
        num2 = int(input("Digite outro número: "))

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
        return "Erro: Divisão por 0."
    except ValueError:
        return "Erro: Valor inválido."
    
print(calculadora())