"""Exercício 3): Escreva um programa que lê um vetor de 10 números inteiros e imprima o número que aparece mais 
vezes (se houver empate, pode ser qualquer um). Além disso, imprima quantas vezes ele aparece."""

numero = 10
vetor = [0]*numero
max_cont = 0
elementos = 0

for i in range(numero):
    vetor[i] = (int(input(str(i) +") ")))

for i in range(numero):
    cont = 0
    for j in range(numero):
        if(vetor[i]==vetor[j]):
            cont = cont + 1

    if(max_cont < cont):
        elementos = vetor[i]
        max_cont = cont

print("numero ", elementos, " e ", max_cont, "vezes")