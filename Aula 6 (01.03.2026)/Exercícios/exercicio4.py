# 4) Verificar se um elemento está presente na lista com while
lista = []
parar = False
soma = 0
encontrou = False
i = 0

elemento = input("Qual elemento você deseja procurar? - ")

while (parar == False):
    lista.append(input(f"Digite o {len(lista) + 1}º elemento - ").lower())
    parar = input("Deseja parar? S/N - ")

    if (parar.lower() == "n"):
        parar = False
    else:
        parar = True

while (i < len(lista)):
    if (elemento.lower() in lista):
        encontrou = True
        break
    i += 1

print("\n")
print("--------- RESULTADO DA BUSCA ---------")

if (encontrou == True):
    print(f"Elemento encontrado na {lista.index(elemento) + 1}ª posição da lista fornecida!")
elif (encontrou == False):
    print("Elemento não encontrado na lista fornecida!")