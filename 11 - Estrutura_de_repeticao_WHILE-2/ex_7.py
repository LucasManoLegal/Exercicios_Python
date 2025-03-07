# 7. Considere dois países: A com 80.000 habitantes e taxa de crescimento anual de 3%, e B com 200.000 habitantes e taxa de 1,5%. Determine quantos anos serão necessários para que a população do país A ultrapasse a população do país B.
populacaoPaisA = 80000
populacaoPaisB = 200000
taxaAnoA = 0.03
taxaAnoB = 0.015
contadorAnos = 0

while populacaoPaisA <= populacaoPaisB:
    populacaoPaisA += populacaoPaisA * taxaAnoA  # Atualiza população de A
    populacaoPaisB += populacaoPaisB * taxaAnoB  # Atualiza população de B
    contadorAnos += 1

print(f"A população do País A superou a população do país B em {contadorAnos} anos.")
