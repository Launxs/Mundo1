#sorteando um item da lista
import random
alunos = []
for i in range(5):
    aluno= input("Nome do aluno que vai concorrer ao sorteiro:")
    alunos.append(aluno)
aluno_sorteado = random.choice(alunos)
print(alunos)
print(f"O aluno sorteado é: {aluno_sorteado}")