# 2) Dado o dicionário abaixo, adicione a chave "profissão" com o valor "engenheiro"
pessoa = {"nome": "Júlia", "idade": 20, "cidade": "Campinas"}
pessoa["profissao"] = "Engenheira de produção"

print("--------- PESSOA ---------")
for valor in pessoa:
    print(f"{pessoa[valor]}")