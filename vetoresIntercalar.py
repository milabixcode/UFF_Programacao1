"""Faça um programa que receba duas listas (vetores) A e B de inteiros, uma de tamanho N e
outra de tamanho M, onde N<=M. O programa deve percorrer as duas listas e intercalar os
elementos de ambas, formando uma terceira lista C. A terceira lista deve começar pelo
primeiro elemento da lista A seguido pelo primeiro elemento da lista B. Quando acabar de
intercalar os elementos, se ainda tiver elementos sobrando na lista maior (B), colocar esses
elementos no fim da lista C."""

n = int(input())
m = int(input())
t = n + m
listaA = [0] * n
listaB = [0] * m
listaC = [] * t

for i in range(n):
    listaA[i] = int(input())
for j in range(m):
    listaB[j] = int(input())
for k in range(n):
    listaC.append(listaA[0])
    listaC.append(listaB[0])
    listaA.pop(0) 
    listaB.pop(0) 
for j in range(m):   
    if listaB != []:
        listaC.append(listaB[0])
        listaB.pop(0)
print(listaC)


