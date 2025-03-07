# 9. Uma loja deseja cadastrar 5 clientes e verificar se o faturamento da loja A foi superior a loja B (faturamento = 54000). Se o faturamento atingir esse valor mostre
# na tela uma mensagem contendo em quanto foi superado o faturamento.
# Inicializando o faturamento das lojas

faturamento_loja_A = 0
faturamento_loja_B = 54000

for i in range(5):  # Loop para coletar o valor da compra de 5 clientes
    valor = float(input(f"Digite o valor da compra do {i+1}º cliente para a loja A: "))
    faturamento_loja_A += valor  # Adiciona o valor da compra ao faturamento da loja A

if faturamento_loja_A > faturamento_loja_B:  # Verifica se o faturamento da loja A é maior que o faturamento da loja B
    superacao = faturamento_loja_A - faturamento_loja_B  # Calcula a diferença entre os faturamentos
    print(f"O faturamento da loja A foi superior ao da loja B em R${superacao:.2f}.")  # Imprime a mensagem de superação
else:
    print(f"O faturamento da loja A não foi superior ao da loja B.")  # Imprime a mensagem informando que o faturamento não foi superior
