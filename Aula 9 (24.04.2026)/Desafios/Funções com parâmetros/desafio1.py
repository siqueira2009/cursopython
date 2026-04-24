# 1) Criar uma função recursiva (que retorne ela mesma) para armazenar N termos da sequência de
# Fibonacci em uma lista. N é definido pelo usuário. Ao encontrar os termos, imprimir a lista
# e finalizar a função

def fibonnaci(qtd):

    if (len(sequencia) == 0):
        sequencia.append(0)
    elif (len(sequencia) == 1):
        sequencia.append(1)
    else:
        sequencia.append(sequencia[len(sequencia) - 1] + sequencia[len(sequencia) - 2])
    
    while (len(sequencia) != qtd):
        fibonnaci(qtd)

qtdNumeros = 0

while (qtdNumeros < 1):
    qtdNumeros = int(input("Quantos números na sequência de Fibonnaci deseja ver? "))

sequencia = []

fibonnaci(qtdNumeros)

print(f"\n--------- SEQUÊNCIA DE FIBONNACI COM {qtdNumeros} NÚMEROS ---------")
print(sequencia)