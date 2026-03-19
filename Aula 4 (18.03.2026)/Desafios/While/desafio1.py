# 1. Faça um programa que calcule o maior palíndromo resultado do produto de dois números de 3 dígitos
i = 100
j = 100
maiorPalindromo = 11
numero1 = 0
numero2 = 0
palindromos = []

while (i <= 999):
    while (j <= 999):
        temp = i * j
        reversedTemp = str(temp)[::-1]

        if (reversedTemp == str(temp)):
            palindromos.append(temp)
        j = j + 1
    i = i + 1
    j = 100    

print(f"--------- MAIOR PALÍNDROMO PRODUTO DE UM DOIS NÚMEROS DE 3 DÍGITOS ---------")
print(f"O maior palíndromo é {max(palindromos)}")