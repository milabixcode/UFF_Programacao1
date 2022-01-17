"""Receba uma matriz A (NxM) de inteiros e ordene seus elementos de forma que os maiores fiquem na primeira coluna, 
depois os próximos maiores na segunda coluna e assim por diante (e cada coluna também esteja ordenada)."""

"""número de linhas"""
n = int(input())
"""número de colunas"""
m = int(input())

"""inicializando a matriz"""
A = []
for i in range(n):
    A.append([0]*m)

"""inicializando a lista"""
lista = []
for i in range(n*m):
    lista.append(int(input()))
"""ordenando a lista de maneira reversa"""
for i in range(n*m):
    for j in range((n*m)-1):
        if lista[j] < lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
"""preenchendo a matriz já com a lista ordenada"""
for i in range(m):
    for j in range(n):
        A[j][i] = lista[i*n + j]

print(A)

