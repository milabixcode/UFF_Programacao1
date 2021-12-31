"""Faça um programa que receba uma matriz NxM de inteiros e some cada um dos “N” elementos
de cada uma das “M” colunas pelo menor elemento em módulo daquela coluna. Imprima a
matriz modificada"""
import math
n = int(input())
m = int(input())

matrix = []

for i in range(n):  
    linha = []      
    for j in range(m):
        linha.append(int(input()))
    matrix.append(linha)

lista = []
for j in range(m):
    menor = int(math.fabs(matrix[0][j]))
    for i in range(n):
        if math.fabs(matrix[i][j]) < menor:
            menor = int(math.fabs(matrix[i][j]))
    lista.append(menor)

for j in range(m):
    for i in range(n):
        matrix[i][j] = matrix[i][j] + lista[j]
print(matrix)

