"""-Vamos fazer um programa para guardar os nomes e as notas de 40 alunos e dar os
parabéns aqueles que tiraram nota acima da média:"""

numero = 40
nomes = []
notas = []
media = 0

for i in range(numero):
    nomes.append('nome: ')
    notas.append((float(input('nota'))))
    media = media + notas[i]

media = media/numero
print('A média da turma é ', media)

for i in range(numero):
    if notas[i] > media:
        print('Parabéns', nomes[i])