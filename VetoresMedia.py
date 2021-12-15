"""Faça um programa que recebe uma lista de números reais distintos positivos de tamanho 5. O
programa deve percorrer esta lista e imprimir o valor mais próximo da média dos valores deste
vetor
ENTRADA: 5 números reais positivos (>= 0) e distintos (pode acreditar)
SAIDA: número real (com 2 casas decimais) que representa o valor do vetor que tem a menor
distância para a média do vetor"""

import math
n = 5
listaNumeros = [0] * n
soma = 0
media = 0


for i in range(n):
    listaNumeros[i] = float(input())
for i in range(n):
    elemento = listaNumeros[i]
    soma = soma + elemento

media = soma/n
menor = listaNumeros[0]

diferencaInicial = math.fabs(media - listaNumeros[0])
for i in range(n):
    diferenca = math.fabs(media - listaNumeros[i])
    if(diferenca <= diferencaInicial):
        menor = listaNumeros[i]
        diferencaInicial = diferenca

print('%.2f' %menor)




