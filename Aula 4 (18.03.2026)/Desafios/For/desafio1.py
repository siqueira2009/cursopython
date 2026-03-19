# 1. Faça um programa que calcule a soma dos divisores de um número inteiro definido pelo usuário
numero = int(input("Digite um número para calcular a soma dos seus divisores: "))
soma = numero

for i in range(1, numero):
    if (numero % i == 0):
        soma = soma + i

print("--------- SOMA DOS DIVISORES ---------")
print(f"A soma dos divisores de {numero} é {soma}")