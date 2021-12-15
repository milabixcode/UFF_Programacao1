"""Exercício 2): A coordenação do curso de computação deseja saber quantos alunos estão cursando ( de forma 
irregular ) as disciplinas de PROG1 e PROG2 ao mesmo tempo. Faça um programa que:
(i) leia as matriculas (inteiro) dos 30 alunos de PROG1 e dos 40 alunos de PROG2,
(ii) imprima as matrículas dos alunos irregulares e
(iii) imprima no fim a quantidade de alunos irregulares"""

alunosP1 = 30
alunosP2 = 40
cont = 0
p1 = [0]*alunosP1
p2 = [0]*alunosP2
print('Prog1')
for i in range(alunosP1):
    p1[i] = (int(input(str(i) +") ")))
print('Prog2')
for i in range(alunosP2):
    p2[i] = (int(input(str(i)+") ")))

for i in range(alunosP1):
    for j in range(alunosP2):
        if(p1[i])==p2[j]:
            print("Aluno ", p1[i], "irregular")
            cont = cont+1
print("total=", cont)