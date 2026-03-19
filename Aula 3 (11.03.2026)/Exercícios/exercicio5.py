# 5. Verificar se um aluno foi aprovado, reprovado ou está em recuperação
nota = float(input("Digite a sua nota: "))

if (nota < 0):
    print("...")
elif (nota >= 0 and nota < 4):
    print("Reprovado!")
elif (nota >= 4 and nota < 6):
    print("Recuperação!")
else:
    print("Aprovado!")