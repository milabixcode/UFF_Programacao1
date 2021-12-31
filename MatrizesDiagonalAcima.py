"""Faça um programa que recebe como parâmetro uma matriz NxN de números inteiros. Esse
programa deve informar:
- a soma dos elementos acima da diagonal principal.
- o número de células da matriz que têm valor menor que a média dos valores das
células da matriz"""

n = int(input())

matrix = []

for i in range(n):  
    linha = []      
    for j in range(n):
        linha.append(int(input()))
    matrix.append(linha)

soma = 0
for i in range(n):
    for j in range(n):
        if j > i:
            soma = soma + matrix[i][j]

media = 0
for i in range(n):
    for j in range(n):
        media = media + matrix[i][j]
media = media/(n*n)

contador = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] < media:
            contador = contador + 1
        
print(soma)
print(contador)
