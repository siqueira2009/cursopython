# 2. Calcule o fatorial de um número escolhido pelo usuário
numero = int(input("Digite um número inteiro para calcular o seu fatorial: "))
i = numero
resultado = 1

while (i > 0):
    resultado = resultado * i
    i = i - 1

print("--------- FATORIAL ---------")
print(f"O fatorial de {numero} é {resultado}")