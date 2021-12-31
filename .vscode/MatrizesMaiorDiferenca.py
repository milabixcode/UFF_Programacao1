"""Faça um programa que leia uma matriz NxM de inteiros, descubra o maior elemento da
matriz,diminua cada elemento da matriz por este maior elemento, imprima a matriz"""

n = int(input())
m = int(input())

matrix = []

for i in range(n):  
    linha = []      
    for j in range(m):
        linha.append(int(input()))
    matrix.append(linha)

maior = 0
for i in range(n):
    for j in range(m-1):
        if matrix[i][j] < matrix[i][j+1]:
            maior = matrix[i][j+1]
        else:
            maior = matrix[i][j]

for i in range(n):
    for j in range(m):
        matrix[i][j] = matrix[i][j] - maior
print(matrix)