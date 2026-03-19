# 2. Verificar se um ano é bissexto ou não
ano = int(input("Digite um ano: "))

if (ano % 100 != 0 and ano % 4 == 0):
    print(f"O ano {ano} é bissexto!")
elif (ano % 100 == 0 and ano % 400 == 0):
    print(f"O ano {ano} é bissexto!")
else:
    print(f"O ano {ano} não é bissexto!")