"""Faça um programa que leia uma matriz NxN de inteiros, troque os elementos da diagonal
principal e da diagonal secundária, e inverta os elementos da primeira linha. Depois imprima a
matriz"""

n = int(input())

matrix = []

for i in range(n):  
    linha = []      
    for j in range(n):
        linha.append(int(input()))
    matrix.append(linha)

for i in range(n):
    matrix[i][i], matrix[i][n-1-i] = matrix [i][n-1-i], matrix[i][i]

linhaNova = []
for j in range(n-1,-1,-1):        
    linhaNova.append(matrix[0][j])

matrix[0] = linhaNova

    
print(matrix)
