# 2. Criar uma lista com os quadrados de cada número de uma outra lista (gerada pelo usuário)
numeros = []
quadrados = []
i = 1

for i in range(100):  # Loop até 100 iterações ou até "P" ser digitado
    numeroAtual = input(f"Digite o {i + 1}º número ('P' para parar): ")

    if (numeroAtual.lower() == "p"):
        break
    else:
        numeros.append(float(numeroAtual))
        i += 1

for numero in numeros:
    quadrados.append(numero ** 2)

print("--------- QUADRADOS ---------")
print("O quadrado dos números digitados é: ")

for i in range(0, len(numeros)):
    print(f'{numeros[i]} -- {quadrados[i]}')