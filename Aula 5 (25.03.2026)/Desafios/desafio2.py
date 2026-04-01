# Desafio 2) - Criar um sistema de comando de uma loja de jogos.
# O programa deve conter pelo menos 6 listas: 
#     a) uma indicando quais jogos estão disponíveis para venda;
#     b) uma para mostrar o preço de cada jogo
#     c) uma para mostrar a quantidade de jogos disponíveis na loja para venda;
#     d) uma informando o preço de fábrica dos jogos para aumentar o estoque;
#     e) uma para registrar as vendas;
#     f) uma para registrar as compras de estoque.
# Todas as informações de um jogo devem estar no mesmo índice nas listas.
# Criar um menu interativo com as seguintes opções para o usuário: 
#     a) registrar venda;
#     b) compra de estoque;
#     c) resumo da loja;
#     d) sair.
# Ao sair indicar que o caixa está fechado. 
# O usuário deve controlar o sistema da loja, registrando as vendas e as compras de estoque, sem esquecer de alterar os valores da lista de quantidade.

jogos = ["God of War", "Stardew Valley", "Minecraft"]
precos = [199.90, 24.99, 99.00]
quantidade = [10, 4, 7]
precosFabrica = [150.00, 15.00, 60.00]
vendas = []
compras = []

continuar = True

while (continuar == True):
    print('')

    print("| --------- MENU LOJA DE JOGOS ---------- |")
    print("| 1) Registrar venda -------------------- |")
    print("| 2) Compra de estoque ------------------ |")
    print("| 3) Resumir status da loja ------------- |")
    print("| 4) Sair ------------------------------- |")

    print('')

    opcao = int(input("O que deseja fazer? - "))
    print('')

    if opcao == 1:
        jogoComprado = input("Qual jogo foi comprado? - ")

        if jogoComprado in jogos:
            quantidadeComprada = int(input("Quantas unidades foram compradas? - "))
            indiceJogo = jogos.index(jogoComprado)

            if quantidadeComprada < quantidade[indiceJogo]:
                quantidade[indiceJogo] -= quantidadeComprada
                jogos.remove(jogoComprado)
                vendas.append(jogoComprado)
                print("Venda registrada!")
            else:
                print("Erro! Quantidade comprada maior que quantidade existente. Tente novamente!")
        else:
            print("Jogo não encontrado! Tente novamente.")

        pass
    elif opcao == 2:
        jogoAdquirido = input("Qual jogo deseja comprar? - ")
        quantidadeAdquirida = int(input("Quantas unidades foram compradas? - "))

        if jogoAdquirido in jogos:
            indiceJogo = jogos.index(jogoAdquirido)
            quantidade[indiceJogo] += quantidadeAdquirida
        else:
            jogos.append(jogoAdquirido)
            quantidade.append(quantidadeAdquirida)

        compras.append(jogoAdquirido)
        
        pass
    elif opcao == 3:
        print("| STATUS DA LOJA ")
        print(f"| Jogos: {', '.join(jogos)}")
        print(f"| Preços (em R$): {', '.join(map(str, precos))}")
        print(f"| Preços de Fábrica (em R$): {', '.join(map(str, precosFabrica))}")
        print(f"| Quantidade: {', '.join(map(str, quantidade))}")
        print(f"| Vendas: {', '.join(vendas)}")
        print(f"| Compras: {', '.join(compras)}")
        pass
    elif opcao == 4:
        print("Fechando sistema...")
        continuar = False
        pass
    else:
        print("Fechando sistema...")
        continuar = False
        pass