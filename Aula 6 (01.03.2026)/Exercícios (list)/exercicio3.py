# 3) Dada uma lista de números, crie uma nova lista com apenas os números impares
numeros  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
impares = [n for n in numeros if n % 2 != 0]

print("--------- ÍMPARES ---------")
print(impares)