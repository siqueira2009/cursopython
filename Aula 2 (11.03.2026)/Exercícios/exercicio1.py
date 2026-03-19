# Pegar 3 notas e calcular a sua média
import math

nota1 = float(input("Digite a nota do primeiro aluno: "))
nota2 = float(input("Digite a nota do segundo aluno: "))
nota3 = float(input("Digite a nota do terceiro aluno: "))

soma = nota1 + nota2 + nota3
media = soma / 3

print("---------------- MÉDIA ----------------")

print(f'A média dos alunos foi {media: .2f}!')
print(f'A média arredondada (para baixo) foi {math.floor(media)}!')
print(f'A média arredondada (para cima) foi {math.ceil(media)}!')