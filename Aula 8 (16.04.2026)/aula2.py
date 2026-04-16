# Dicionários
# Guarda chaves e valores
# São mutáveis (permite alteração, adição e remoção de valores)

meuDicionario = {
    "nome": "Lucas",
    "idade": 16,
    "cidade": "Campinas"
}

print(meuDicionario["nome"])


meuDicionario2 = dict(nome="Lucas", idade=16, cidade="Campinas")

print(meuDicionario.get("nome", "Não existe"))

meuDicionario3 = {}.fromkeys([0,1,2,3],'dado');
print(meuDicionario3)

dados = None
print(type(dados))
dados = 15
print(type(dados))

meuDicionario4 = {
    (1,2): "HP",
    (3, 4): "PJ",
    (5, 6): "SA"
}

meuDicionario4[(7, 8)] = "MR"
meuDicionario4[(3, 4)] = "Pokémon"
print(meuDicionario4)

meuDicionario4.update({(1, 2): 'Digimon'})
print(meuDicionario4)


pokemons = {
    "Água": "Squirtle",
    "Fogo": "Charmander",
    "Grama": "Bulbassauro"
}

dado = pokemons.pop("Água")
print(dado)


del pokemons["Grama"]
print(pokemons)

meuDicionario5 = {"Programar": "JavaScript"}
meuDicionario5.clear()
print(meuDicionario5)

personagem = {"Nome": "Rick", "Funcao": "Cientista", "Neto": "Morty"}

for item in personagem:
    print(item)
    print(personagem[item])

print(personagem.keys())
print(personagem.values())

print("Tamanho:", len(personagem))

numeros = {"a": 1, "b": 2, "c": 3, "d": 4}

print(max(numeros.values()))
print(min(numeros.values()))
print(sum(numeros.values()))