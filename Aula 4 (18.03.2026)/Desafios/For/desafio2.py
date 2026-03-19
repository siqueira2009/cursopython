# 2. Faça um programa que imprima os n primeiros múltiplos de 5, sendo n definido pelo usuário
quantidade = int(input("Digite a quantidade de múltiplos de 5 que você deseja ver: "))


print(f"--------- {quantidade} MÚLTIPLOS DE 5 ---------")
for i in range(1, quantidade):
    print(f"{i} x 5 = {i * 5}")
print(f"{quantidade} x 5 = {quantidade * 5}")