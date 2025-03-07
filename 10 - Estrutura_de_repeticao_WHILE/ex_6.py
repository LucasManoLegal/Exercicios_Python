num = 1
soma = 0

while num <= 100:
    if num % 2 == 0: # A variável soma só vai ser incrementada quando o resto da divisão for 0.
        soma += num
    num += 1 # incrementa ao contador.
print(soma)