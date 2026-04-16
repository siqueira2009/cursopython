# 3) Dado o dicionário abaixo, remova a chave "idade"
pessoa = {"nome": "Júlia", "idade": 20, "cidade": "Campinas"}
pessoa["profissao"] = "Engenheira de produção"
del pessoa["idade"]

print("--------- PESSOA ---------")
for valor in pessoa:
    print(f"{pessoa[valor]}")