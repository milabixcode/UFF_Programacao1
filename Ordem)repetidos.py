"""Faça um programa que receba um vetor de inteiros de tamanho N, retire os elementos
repetidos, ordene e imprima o resultado.
OBS: Use qualquer método de ordenação"""


n = int(input())
vetor = [0] * n
vetorSemRepetidos =[]

for i in range(n):
    vetor[i] = int(input())

for k in range(n):    
    for j in range(n-1):
        if vetor[j] > vetor[j+1]:
            vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
    
for i in range(n-1):
    if vetor[i] == vetor[i+1]:
        continue
    else:
        vetorSemRepetidos.append(vetor[i])

tamanhoSemRepetidos = len(vetorSemRepetidos) - 1
tamanhoVetor = n-1
if (vetorSemRepetidos == []):
    vetorSemRepetidos.append(vetor[tamanhoVetor])
if (vetor[tamanhoVetor] != vetorSemRepetidos[tamanhoSemRepetidos]):
    vetorSemRepetidos.append(vetor[tamanhoVetor])

print(vetorSemRepetidos)

