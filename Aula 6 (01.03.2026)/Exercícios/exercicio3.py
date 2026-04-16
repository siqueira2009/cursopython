# 3) Contagem de vogais em uma lista de palavras com while.
# Crie um programa que receba uma lista de palavras e retorne a quantidade total de vogais em todas as palavras usando um loop while.
import unicodedata

palavras = []
vogais = ['a', 'e', 'i', 'o', 'u']
parar = False
totalVogais = 0
i = 0

def removerAcentos(texto):
    textoSemAcentos = unicodedata.normalize('NFD', texto)

    return textoSemAcentos.encode('ascii', 'ignore').decode('utf-8')

while (parar == False):
    palavras.append(input("Digite uma palavra - "))
    parar = input("Deseja parar? (S/N): ")

    if (parar.lower() == "s"):
        parar = True
    else:
        parar = False

while (i < len(palavras)):
    j = 0
    while (j < len(palavras[i])):
        if removerAcentos(palavras[i][j]) in vogais:
            totalVogais += 1
        j += 1

    i += 1

print("--------- VOGAIS ---------")
print("O total de vogais nas palavras digitados é", totalVogais)