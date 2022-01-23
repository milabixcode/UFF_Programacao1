
n = int(input())

A = []
for i in range(n):  
    linha = []      
    for j in range(n):
        linha.append(int(input()))
    A.append(linha)

soma = 0
contador = 0

for i in range(n):
    for j in range(n):
        if (j > i and i + j <= n-2) or (i + j > n-1 and j < i):
            soma = soma + A[i][j]
            contador = contador + 1

media = soma/contador
    
print("%.2f" %media)