# 1. Calcular a média de uma lista de números (quantos números o usuário desejar)
numeros = []
soma = 0

for i in range(100) :
    numeroAtual = input(f"Digite o {i + 1}º número ('P' para parar): ")

    if (numeroAtual.lower() == "p"):
        break
    else:
        numeros.append(float(numeroAtual))

for numero in numeros:
    soma = soma + numero

media = soma / len(numeros)
print("--------- MÉDIA ---------")
print("A média dos números digitados é", round(media, 2))