# 1. Calcule a soma dos números de 1 a 10
totalNumeros = int(input("Quantos números você quer somar? "))
soma = 0
i = 0

while (i <= totalNumeros):
    soma = soma + i
    i = i + 1

print("--------- SOMA DE 1 A 10 ---------")
print(f"A soma de 1 até {totalNumeros} é {soma}")