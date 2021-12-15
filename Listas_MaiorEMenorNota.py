"""Receba do usuário um vetor de notas de 10 alunos e imprima a maior e a menor nota"""
n = [0.0]*10
maior = -1.0
menor = 11.0
for i in range(0,10):
    n[i] = float(input("nota?"))
    if (n[i]<menor):
        menor = n[i]
    if (n[i]>maior):
        maior=n[i]
print("maior=", maior, "menor=", menor)