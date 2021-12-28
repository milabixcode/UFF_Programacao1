"""Faça um programa que receba um vetor de inteiros positivos de tamanho N, e ordene seguindo
o seguinte critério.
- primeiro os pares
- depois os ímpares
Sendo que devem ser apresentados os pares em ordem crescente e os ímpares em ordem
decrescente.
OBS: Use qualquer método de ordenação"""

n = int(input())
vetor = [0] *n

for i in range(n):
    vetor[i] = int(input())

for i in range(n):
    for j in range(n-1):
        if vetor[j] > vetor[j+1]:
            vetor[j], vetor[j+1] = vetor[j+1], vetor[j]

vetorPares = []
vetorImpares = []
for i in range(n):
    if vetor[i] % 2 == 0 or vetor[i] == 0:
        vetorPares.append(vetor[i])
    else:
        vetorImpares.append(vetor[i])

for i in range(len(vetorImpares)):
    for j in range(len(vetorImpares)-1):
        if vetorImpares[j] < vetorImpares[j+1]:
            vetorImpares[j], vetorImpares[j+1] = vetorImpares[j+1], vetorImpares[j]

vetorFinal = []
for i in range(len(vetorPares)):
    vetorFinal.append(vetorPares[i])
for i in range(len(vetorImpares)):
    vetorFinal.append(vetorImpares[i])

print(vetorFinal)
    