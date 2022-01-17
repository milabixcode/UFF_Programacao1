"""Faça um programa que leia a matriz A de inteiros e de dimensão NxN. Calcule a Matriz B = AxA e depois calcule a 
matriz C = B + AT, onde AT é a matriz transposta de A. No fim, imprima a matriz C."""

n = int(input())

A = []
for i in range(n):
    lista = []
    for j in range(n):
        lista.append(int(input()))
    A.append(lista)

B = []
for i in range(n):
    B.append([0]*n)
for i in range(n):
    for j in range(n):
        for k in range(n):
            B[i][j] = B[i][j] + (A[i][k]*A[k][j]) #produto escalar da linha i de A pela coluna j de A

ATransposta = []
for i in range(n):
    ATransposta.append([0]*n)
for i in range (n):
    for j in range(n):
        Aux = A[j][i]
        ATransposta[i][j] = Aux

C = []
for i in range(n):
    C.append([0]*n)
for i in range (n):
    for j in range(n):
        C[i][j] = B[i][j] + ATransposta[i][j] 

print(C)

