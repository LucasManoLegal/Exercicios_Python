# 9. Implemente um sistema onde o usuário insere o código e a quantidade dos produtos desejados. O programa deve calcular o valor total e permitir que o usuário finalize o pedido digitando 0.

preco1 = 7.00
preco2 = 5.00
preco3 = 6.00
preco4 = 8.00

total = 0
subtotal = 0
print("                   Produtos")
print("----------------------------------------------")
print(" Código: 1 | Produto: Banana  | Preço: R$ 7.00 ")
print(" Código: 2 | Produto: Laranja | Preço: R$ 5.00 ")
print(" Código: 3 | Produto: Pera    | Preço: R$ 6.00 ")
print(" Código: 4 | Produto: Abacaxi | Preço: R$ 8.00 ")
print("----------------------------------------------")
# Início do loop para inserir código dos produtos
codigo = int(input("Digite o código do produto: "))

while codigo != 0:
    if codigo == 1:
        print(" Código inserido: 1 | Produto: Banana | Preço: R$ 7.00 ")
        qtd = int(input("Agora digite a quantidade de itens: "))
        subtotal += (preco1 * qtd) # Atualizando o subtotal diretamente
        total += subtotal # Atualizando o total diretamente
        print(f"Quantidade: {qtd} | Produto: Banana | Subtotal: R$ {subtotal} ")  
    elif codigo == 2:
        print(" Código inserido: 2 | Produto: Laranja | Preço: R$ 5.00 ")
        qtd = int(input("Agora digite a quantidade de itens: "))
        subtotal += (preco2 * qtd) # Atualizando o subtotal diretamente
        total += subtotal # Atualizando o total diretamente
        print(f"Quantidade: {qtd} | Produto: Laranja | Subtotal: R$ {subtotal} ")  
    elif codigo == 3:
        print(" Código inserido: 3 | Produto: Pera | Preço: R$ 6.00 ")
        qtd = int(input("Agora digite a quantidade de itens: "))
        subtotal += (preco3 * qtd) # Atualizando o subtotal diretamente  
        total += subtotal # Atualizando o total diretamente
        print(f"Quantidade: {qtd} | Produto: Pera | Subtotal: R$ {subtotal} ")  
    elif codigo == 4:
        print(" Código inserido: 4 | Produto: Abacaxi | Preço: R$ 8.00 ")
        qtd = int(input("Agora digite a quantidade de itens: "))
        subtotal += (preco4 * qtd) # Atualizando o subtotal diretamente 
        total += subtotal # Atualizando o total diretamente
        print(f"Quantidade: {qtd} | Produto: Abacaxi | Subtotal: R$ {subtotal} ")  
    else:
        print("Código inválido!")  # Caso o código do produto não seja válido
    # Iniciando novamente o loop
    codigo = int(input("Digite o código do produto (digite 0 para finalizar): "))
print(f"Valor total: R$ {total:.2f}")
    


