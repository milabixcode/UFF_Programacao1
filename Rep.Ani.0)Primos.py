#Faça um programa que receba dois inteiros A e B e imprima todos os números primos entre os
#números A e B (incluindo A e B)
#ENTRADA: números inteiros A e B onde 1<= A<= B (Pode acreditar)
#SAIDA: número(s) (inteiros), um por linha, indicando os números primos entre A e B

a = int(input())
b = int(input())
for i in range(a,b+1):
    primo = 0
    for j in range(2,i):
        if(i%j == 0):
            primo = primo + 1
    if(primo == 0) and (i != 1):
        print(i)
