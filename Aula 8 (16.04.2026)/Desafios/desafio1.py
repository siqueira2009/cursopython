# 1) Faça um programa que contabiliza time de heróis e vilões da seguinte forma:
# - Crie um dicionário chamado herói com chave sendo o nome do personagem e o elemento o nível de poder
#   do personagem entre 1 a 100. Ex: herói = {‘Flash’:85}.
# - Crie outro dicionário que serão as armas que podem ser usadas pelo herói, sendo a chave o nome da arma
#   e o elemento o nível de poder de 0 a 100. Ex: arma = {‘Escudo do Capitão América’:60}
# - Crie um último dicionário representado os vilões sendo a chave o nome e o elemento o nível de poder de 0 a 200.
#   Ex: vilao={‘Thanos’:175}
# Após isso o usuário poderá escolher um herói, uma arma soma os pontos de poder e escolher um vilao para lutar,
# apresente quem foi o vencedor, caso for o herói imprima a arma usada. Caso resulte em empate informe na saída.
# Observação: Pode definir qualquer herói,vilao e arma que quiser

herois = [{"nome": "Capitão América", "poder": 90 }, {"nome": "Capitã Marvel", "poder": 95}, {"nome": "Batman", "poder": 90}, {"nome": "Homem de ferro", "poder": 85}]

armas = [{"nome": "Mjölnir", "poder": 80}, {"nome": "Escudo do Capitão América", "poder": 70}, {"nome": "Chicote da Mulher Maravilha", "poder": 65}, {"nome": "O Um Anel", "poder": 95}]

viloes = [{"nome": "Thanos", "poder": 175}, {"nome": "Galactus", "poder": 190}, {"nome": "Lex Luthor", "poder": 130}, {"nome": "Ultron", "poder": 150}]


for i, dic in enumerate(herois):
    print(f"| Opção {i}: {dic['nome']} - {dic['poder']} de poder")
heroi = int(input("\n| Escolha um herói para lutar: "))

print("\n")

for i, dic in enumerate(armas):
    print(f"| Opção {i}: {dic['nome']} - {dic['poder']} de poder")
arma = int(input("\n| Escolha uma arma para usar: "))

print("\n")

for i, dic in enumerate(viloes):
    print(f"| Opção {i}: {dic['nome']} - {dic['poder']} de poder")
vilao = int(input("\n| Escolha um vilão para enfrentar: "))

print("\n\n")

poderUsuario = herois[heroi]["poder"] + armas[arma]["poder"]
poderInimigo = viloes[vilao]["poder"]
diferencaPoder = poderUsuario - poderInimigo

print("--------- QUE COMEÇE A BATALHA ---------")
print(f"{viloes[vilao]["nome"]} ({poderInimigo}) vs {herois[heroi]["nome"]} ({poderUsuario})")


if (diferencaPoder == 0):
    print("Nada mais justo que um empate!")
elif (diferencaPoder > 0):
    print(f"Você ganhou com o {herois[heroi]["nome"]} com uma diferença de poder de {diferencaPoder}!")
elif (diferencaPoder < 0):
    print(f"Você perdeu para o {viloes[vilao]["nome"]} com uma diferença de poder de {abs(diferencaPoder)}!")