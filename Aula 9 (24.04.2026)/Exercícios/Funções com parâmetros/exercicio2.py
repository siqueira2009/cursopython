# 2) Crie uma função que receba uma string e um caractere como parâmetros e retorne o número de vezes que o caractere aparece na string

palavra = input("Digite uma palavra: ")
letra = input("Digite uma letra para filtrar: ")[0]

def qtdLetras(palavra, letra):
    qtdRepeticoes = 0
    novaPalavra = list(palavra.lower())
    
    for i in range(len(palavra)):
        if (letra.lower() == palavra[i].lower()): 
            qtdRepeticoes += 1
            novaPalavra[i] = novaPalavra[i].upper()
    
    novaPalavra = ''.join(novaPalavra)

    return qtdRepeticoes, novaPalavra

quantidadeLetras, novaPalavra = qtdLetras(palavra, letra)

print(f"\n--------- REPETIÇÕES DE {letra} EM {palavra} ---------")
print(f'{quantidadeLetras} repetições de {letra.upper()} ----- {novaPalavra}')