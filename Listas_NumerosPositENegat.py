"""Receba do usuário um vetor de número (positivos e negativos) de tamanho
10 e imprima o maior e o menor número"""

n = [0.0]*10
maior = 0
menor = 0
for i in range(0,10):
    n[i] = float(input("nota?"))
    if (i == 0):
        maior = n[i]
        menor = n[i]
    if (n[i] < menor):
        menor = n[i]
    if (n[i] > maior):
        maior = n[i]
print("maior = ", maior, "menor = ", menor)