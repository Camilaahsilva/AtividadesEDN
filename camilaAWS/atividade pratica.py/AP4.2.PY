# Atividade Prática 04
# AP4.2 - Média da turma

quantidade = int(input("Quantos alunos há na turma? "))

soma_notas = 0

for i in range(quantidade):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    soma_notas += nota

media = soma_notas / quantidade

print("Média da turma:", media)

