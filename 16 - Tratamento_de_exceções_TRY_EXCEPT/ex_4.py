# 4. Crie uma função divisao_segura(a, b) que retorne o resultado da divisão a / b. Se b for zero, a função deve retornar "Erro: Divisão por zero não permitida!".

def divisao_segura():
    try:
        num1 = int(input("Digite um numero: "))
        num2 = int(input("Digite outro numero: "))

        return num1 / num2
    except ZeroDivisionError:
        return "Erro: Divisão por zero não permitida!"

print(divisao_segura())