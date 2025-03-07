# 8. Implemente um sistema de caixa registradora onde o usuário insere valores dos produtos. A entrada de 0 indica o fim da compra. Exiba o total da compra, peça o valor pago e exiba o troco. Após isso, o programa deve reiniciar para um novo cliente.
valorProduto = -1 
# A variável valor produto já é declarada para iniciar o while. Essa é uma outra abordagem para utilizar o laço while. O valor é -1 pois não pode ser 0.
# "valorProduto" poderia receber qualquer outro valor, já que na instrução do while, o valor inserido pelo usuário em "valorProduto" já substitui o valor anterior (-1).
totalCompra = 0
troco = 0
while valorProduto != 0:
    valorProduto = float(input("Digite o valor do produto: (Digite 0 para sair): "))
    totalCompra += valorProduto
print(f"Total da compra: R$: {totalCompra:.2f}")

valorPago = float(input("Agora digite o valor do pago: "))
troco = valorPago - totalCompra
print(f"O troco da compra é de R$: {troco}")