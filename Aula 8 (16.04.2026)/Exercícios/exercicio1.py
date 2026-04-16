# 1) Exercício 1: Crie um dicionário com as seguintes chaves e valores: Chaves: "nome", "idade", "cidade"

pessoa = {"nome": "Júlia", "idade": 20, "cidade": "Campinas"}

print("--------- PESSOA ---------")
for valor in pessoa:
    print(f"{pessoa[valor]}")