# 1. Fazer uma calculadora de 4 operações. Peça a operação desejada e os dois números ao usuário
print("| OPERAÇÕES ------------ |")
print("| 1 -- Soma ------------ |")
print("| 2 -- Subtração ------- |")
print("| 3 -- Multiplicação --- |")
print("| 4 -- Divisão --------- |")
print("| 5 -- Potência -------- |")
print("| 0 -- Sair ------------ |")
print(" ")

escolha = int(input("Escolha uma operação: "))

if (escolha == 0):
    print("Você escolheu sair!")
else:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    match escolha:
        case 1:
            resultado = num1 + num2
            operador = "+"
        case 2:
            resultado = num1 - num2
            operador = "-"
        case 3:
            resultado = num1 * num2
            operador = "x"
        case 4:
            resultado = num1 / num2
            operador = "÷"
        case 5:
            resultado = num1 ** num2
            operador = "^"

    print(" ")
    print("RESULTADO")
    print(f"  {num1}")
    print(f"{operador} {num2}")
    print("--------------")
    print(f"  {resultado}")