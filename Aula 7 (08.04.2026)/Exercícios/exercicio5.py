# 5) Crie uma tupla com os preços de três produtos e encontre o menor preço
precos = []
parar = False

while (parar == False):
    precos.append(float(input(f"Digite o preço do {len(precos) + 1}º produto - ")))
    parar = input("Deseja parar? S/N - ")

    if (parar.lower() == "n"):
        parar = False
    else:
        parar = True
    
precos = tuple(precos)
menorPreco = min(precos)


print("--------- MENOR PREÇO ---------")
print(f'O menor preço é {menorPreco}')
