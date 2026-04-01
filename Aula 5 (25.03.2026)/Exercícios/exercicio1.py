# 1) Usando for, faça a multiplicação de elementos dentro de uma lista.
numeros = []
parar = False
resultado = 1

while (parar == False):
    numeros.append(float(input("Digite um número - ")))
    parar = input("Deseja parar? (S/N): ")

    if (parar.lower() == "s"):
        parar = True
    else:
        parar = False

for numero in numeros:
    resultado *= numero

print("--------- MULTIPLICAÇÃO ---------")
print("A multiplicação dos números digitados é", resultado)