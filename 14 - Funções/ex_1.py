# 1: Crie uma função que receba dois números como parâmetros e retorne a soma deles.

# Solicita ao usuário que digite dois números e converte as entradas para inteiros.
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))

# Define uma função chamada 'somarNumeros' que recebe dois parâmetros: num1 e num2.
def somarNumeros(num1, num2): # a funcão "somarNumeros" recebe dois parametros (inputs) que serão utilizados para que a função funcione.
    # Retorna a soma dos dois números.
    return num1 + num2 # esse é o retorno da função, o cálculo que a funcão realiza, que é exibida uma vez que a função é chamada dentro do código.

# Chama a função 'somarNumeros' com os dois números fornecidos pelo usuário e imprime o resultado.
print("A soma dos numeros é:", somarNumeros(num1, num2)) # dentro dos parênteses da função, o python atribui o valor digitado aos dois parâmetros.