# 1) Receba uma lista de nomes e imprima cada normalize_encoding
nomes = []
parar = False

while (parar == False):
    nomes.append(input(f"Digite o {len(nomes) + 1}º nome - "))
    parar = input("Deseja parar? S/N - ")

    if (parar.lower() == "n"):
        parar = False
    else:
        parar = True

print("--------- NOMES ---------")
for nome in nomes:
    print(nome)
