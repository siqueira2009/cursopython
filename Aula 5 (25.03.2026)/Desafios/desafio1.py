# Desafio 1) - Crie duas listas, uma para o carrinho do supermercado que irá receber produtos comprados e outra para os preços dos produtos.
# Utilizando um loop, preencha as listas com 5 produtos e 5 preços, recebendo estes dados do usuário (input). 
# Por fim, some os preços, imprima o valor total e os produtos do carrinho.
produtos = []
precos = []
somaPrecos = 0

for i in range(5):
    print(f"--------- PRODUTO {i + 1} ---------")
    produtos.append(input(f"Digite o nome do {i + 1}º produto - "))
    precos.append(float(input(f"Digite o preço do {i + 1}º produto - ")))

print("--------- SEU CARRINHO ---------")
for i in range(len(produtos)):
    print(f"{produtos[i]} --- R${precos[i]}")
    somaPrecos += precos[i] 

print(f"TOTAL --- R$ {somaPrecos}")