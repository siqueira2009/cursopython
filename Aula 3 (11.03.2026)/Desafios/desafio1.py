# 1. Verificar se o número digitado é primo ou não
numero = int(input("Digite um número: "))
# numero = abs(numero) # Valor absoluto do número, ou seja, o valor dele até 0
primo = True

# Divide o número por cada número até chegar nele
for i in range(1, numero):
    resto = numero % i

    if ((i != 1 and i != numero) and resto == 0):
        primo = False
        break

# Se for 1, já fala que não é primo
if (numero == 1 or numero == 0 or numero < 0):
    primo = False

# Printa o resultado
if (primo == True):
    print(f"O número {numero} é primo!")
else:
    print(f"O número {numero} não é primo!")