"""Faça um programa que receba N vetores de inteiros de tamanho 5 e os ordene pelo método da
bolha. Para cada vetor ordenado, imprima o número de trocas realizadas entre posições
adjacentes."""

n = int(input())
contador = 0
elementos = 5
vetorDeVetores = []


for i in range(1, n+1):    
    vetorAuxiliar = [0] * elementos 
    vetorDeVetores.append(vetorAuxiliar)      
    for j in range(elementos):
        vetorAuxiliar[j] = int(input())

for i in range(n):
    contador = 0
    vetor = vetorDeVetores[i]
    for j in range(elementos - 1):
        for k in range(elementos - 1):                                                                                             
            if vetor[k] > vetor[k+1]:
                vetor[k], vetor[k+1] = vetor[k+1], vetor[k]
                contador = contador + 1
    print(contador)
