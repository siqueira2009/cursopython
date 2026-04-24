# 1) Crie uma função que receba uma lista como parâmetro e retorne o maior elemento da lista

numeros = []
parar = "n"

print("--------- DIGITE VALORES ---------")

while parar.lower() == "n":
    numero = float(input("\nDigite um número: "))

    numeros.append(numero)

    parar = input("Deseja parar (S/N): ")

    while (parar.lower() != "s" and parar.lower() != "n"):
        print("Valor inválido, responda de novo.")
        parar = input("Deseja parar (S/N): ")


def pegarMaior(list):
    maior = max(list)

    return maior

print("\n--------- MAIOR NÚMERO ---------")
print(pegarMaior(numeros))