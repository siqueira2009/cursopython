# 2) Crie uma lista com os cubos dos números pares de 1 a 10 usando list comprehension
cubos = [x**3 for x in range (1, 11) if x % 2 == 0]
print("--------- CUBOS DOS PARES ---------")
print(cubos)