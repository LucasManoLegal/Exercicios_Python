# 14. Uma loja tem tem uma política de descontos de acordo com o valor da compra do cliente. Os descontos começam acima dos R$500. A cada 100 reais acima dos R$500,00 o
# cliente ganha 1% de desconto cumulativo até 25%.
# Por exemplo: R$500 = 1% || R$600,00 = 2% … etc…
# Faça um programa que exiba essa tabela de descontos no seguinte formato:
# Valordacompra – porcentagem de desconto – valor final

valorCompra = 400 # O valor da compra começa com R$ 400,00 para, ao incrementar 100 imprimir o primeiro valor da tabela (R$ 500,00).
porcentagem = 0

print("Valor da compra | % de desconto | Valor final")  # Imprime o cabeçalho da tabela.
for i in range(25):  
    valorCompra += 100  # Incrementa o valor da compra em R$100 a cada iteração.    
    porcentagem += 0.01 # Incrementa a porcentagem de desconto em 1% a cada iteração.
    valorFinal = valorCompra - (valorCompra * porcentagem)  # Calcula o valor final da compra após aplicar o desconto. Multiplica o valor da compra pela porcentagem de desconto (0.01 representa 1%) e subtrai do valor original.

    print(f"   R$ {valorCompra:.2f}            {i + 1}%          R$ {valorFinal:.2f}")  # Imprime uma linha da tabela formatada.
 