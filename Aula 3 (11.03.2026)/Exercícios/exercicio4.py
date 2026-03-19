# 4. Verificar se um triângulo é equilátero, isóceles ou escaleno
lado1 = float(input("Digite as medidas do primeiro lado do triângulo: "))
lado2 = float(input("Digite as medidas do segundo lado do triâgulo: "))
lado3 = float(input("Digite as medidas do terceiro lado do triângulo: "))

if (lado1 == lado2 and lado2 == lado3):
    print("O triângulo é equilátero!")
elif ((lado1 == lado2 and lado2 != lado3) or (lado1 == lado3 and lado3 != lado2) or (lado2 == lado3 and lado1 != lado2)):
    print("O triângulo é isóceles!")
else:
    print("O triângulo é escaleno!")
