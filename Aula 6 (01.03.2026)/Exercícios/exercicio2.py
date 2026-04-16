# 2) Soma dos elementos de uma lista com for
numeros = []
parar = False
soma = 0

while (parar == False):
    numeros.append(float(input(f"Digite o {len(numeros) + 1}º número - ")))
    parar = input("Deseja parar? S/N - ")

    if (parar.lower() == "n"):
        parar = False
    else:
        parar = True

for numero in numeros:
    soma += numero

print("--------- SOMA DOS NÚMEROS ---------")
print(f"Soma dos números: {soma}")
