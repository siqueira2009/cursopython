# 4) Dada uma lista de palavras, crie uma nova lista com as palavras que têm mais de 5 letras
palavras = ["Lucas", "Computador", "Escola", "Comer", "Oi"]
maisDeCinco = [palavra for palavra in palavras if len(palavra) > 5]

print("--------- PALAVRAS COM MAIS DE 5 LETRAS ---------")
print(maisDeCinco)