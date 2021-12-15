"""Faça um programa que receba uma lista A (vetor) de inteiros de dimensão N e:
(a) inverta os valores de A, troque o primeiro pelo último, o segundo pelo penúltimo e
assim por diante.
(b) após este procedimento, criar um vetor B de dimensão N com o fatorial de cada
valor de A, respeitando as posições, caso o valor for positivo ou nulo. Deixe os valores
negativos intactos.
(c) imprima o vetor B.
ENTRADA: inteiro N (>=1) e depois N números inteiros que irão compor o vetor A
SAIDA: vetor B de inteiros """

n = int(input())
listaA = [0]*n
listaAInvertida = [0]*n
indice = 0

for i in range(n):
    listaA[i] = int(input())
    
for i in range(n-1, -1, -1):
    listaAInvertida[indice] = listaA[i]
    indice = indice + 1

listaB = [0]*n
for indice2 in range(n):
    elemento = listaAInvertida[indice2]
    fatorial = 1
    if elemento < 0:
        fatorial = elemento
    elif elemento == 0:
        fatorial = 1
    else:
        for i in range(1, elemento + 1, 1):
            fatorial = fatorial * i
    listaB[indice2] = fatorial
        
print(listaB)
