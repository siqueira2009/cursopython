#Desafio) Foi realizada uma pesquisa de algumas características e gostos de quatro habitantes incluindo:
# nome, sexo, esporte favorito (Natação, Futebol, Volêi, Tênis) e idade. Com esses dados faça:
# - Função que armazene os dados em uma lista. Dica: Use dicionários dentro da lista.
# - Calcule a idade média de homens que gostam de natação. Caso não haja homens que gostam de natação chame uma função e
#   imprima um aviso de que não há homens que gostam de natação

sexos = ["m", "f"]
esportes = ["natação", "futebol", "vôlei", "tênis"]

print("--------- REGISTRO DE DADOS DE USUÁRIOS ---------")

def coletarDados(pessoa):
    print(f"\n{pessoa + 1}ª pessoa --------")

    nome = input("Digite seu nome: ")
    sexo = input("Digite seu sexo (M/F): ")

    while sexo.lower() not in sexos: 
        print("Valor não disponível! Tente novamente!")
        sexo = input("Digite seu sexo (M/F): ")
    
    esporte = input("Digite seu espor favorito (Natação, futebol, vôlei e tênis): ")

    while esporte.lower() not in esportes:
        print("Valor não disponível! Tente novamente!")
        esporte = input("Digite seu espor favorito (Natação, futebol, vôlei e tênis): ")

    idade = int(input("Digite a sua idade: "))

    return {"nome": nome, "sexo": sexo, "esporte": esporte, "idade": idade}

def rodarPorPessoa(qtd):
    dados = []

    for i in range(qtd):
        dados.append(coletarDados(i))

    return dados

def homensNatacao(qtd = 4):
    dados = rodarPorPessoa(qtd)
    qtdHomens = 0
    somaHomens = 0

    for i in range (len(dados)):
        if (dados[i]['sexo'].lower() == "m" and dados[i]['esporte'].lower()):
            qtdHomens += 1
            somaHomens += dados[i]["idade"]

    if (somaHomens > 0):
        mediaHomens = somaHomens / qtdHomens
        print("\nMédia da idade dos homens que gostam de natação: " + mediaHomens)
    else:
        print("Não existem homens que gostme de natação :/")


homensNatacao()