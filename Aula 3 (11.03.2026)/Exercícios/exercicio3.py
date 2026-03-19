# 3. Verificar faixa etária de uma pessoa
idade = int(input("Digite a sua idade (em anos): "))

if (idade < 0):
    print("Feto")
elif (idade > 0 and idade <= 2):
    print("Bebê")
elif (idade > 2 and idade <= 12):
    print("Criança")
elif (idade > 12 and idade <= 18):
    print("Adolescente")
elif (idade > 18 and idade <= 70):
    print("Adulto")
else:
    print("Idoso")