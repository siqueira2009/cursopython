# 1) Kiko precisa invadir uma prisão de segurança extremamente alta para resgatar Jaiminho. 
# Porém, existem 3 portões protegidos por senhas do TIPO TUPLA. 
# Cada portão oferece uma dica para descobrir a senha. 
# A dica é composta por uma tupla contendo algumas dezenas, e uma frase indicando o processo a ser realizado. 
# Kiko deve criar um programa que imprima na tela as três senhas no seguinte formato: print(f'Portão X: {senha_do_portão_X}').

# Dicas
# Portão 1 = (29, 54, 45) [Alterar todas as dezenas para 0]
# Portão 2 = (12, 28, 37, 54) [A soma dos elementos 2 e 3 é o primeiro elemento da senha, a soma  dos elementos 1 e 4 é o segundo elemento da senha]
# Portão 3 = (16, 86, 78, 32, 85, 12) [O valor mínimo é o primeiro elemento da senha, o valor máximo é o segundo elemento da senha]

dica1 = (29, 54, 45)
dica2 = (12, 28, 37, 54)
dica3 = (16, 86, 78, 32, 85, 12)

portao1 = tuple(num % 10 for num in dica1)
portao2 = tuple(dica2[2] + dica2[3], dica2[0] + dica2[3])
portao3 = tuple(min(dica3), max(dica3))

print(f"Portão 1: {portao1}")
print(f"Portão 2: {portao2}")
print(f"Portão 3: {portao3}")