# IF: bloco de comandos que será executado caso uma condição seja verdadeira
numero = 10

if (numero > 0):
    print("Número maior que 10!")

# ELSE: bloco de comandos que será executado caso o IF seja falso
senha = "1234"

if (senha == "1234"):
    print("Senha correta!")
else:
    print("Senha incorreta!")

# ELIF: bloco de comandos que será executado caso o IF seja falso e deseja verificar OUTRA condição
numero = 0

if (numero > 0):
    print("Número positivo!")
elif (numero == 0):
    print("O número é 0!")
else:
    print("O número é negativo!")