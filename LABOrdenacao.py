"""Escreva um programa que leia um valor inteiro N, depois receba um vetor de
inteiros de tamanho N. O programa deve perguntar por qual método o usuário deseja ordenar
o vetor (1-bolha, 2-seleção 3-Sair). O programa deve ordenar o vetor pelo método selecionado,
contando o número de comparações (if’s) realizadas. No fim, perguntar se o usuário deseja
repetir a operação com outro método."""

N = int(input())
vetor = [] * N
metodo = int(input('Qual método deseja ordenar? 1-bolha 2-seleção 3-Sair ' ))
replay = 0

while replay == 1:
    N = int(input())
    vetor = [] * N
    metodo = int(input('Qual método deseja ordenar? 1-bolha 2-seleção 3-Sair ' ))

for i in range(N):
    vetor.append(int(input()))
if (metodo == 1):
    for i in range(N):
        for j in range (N-1):
            if (vetor[j + 1] > vetor[j]):
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
if (metodo == 2):
    for i in range (N-1):
        for j in range (i+1, N):
            if (vetor[i] > vetor[j]):
                t = vetor[i]
                vetor[i] = vetor[j]
                vetor[j] =  t
if (metodo == 3):
    print("FIM")

replay = int(input('Deseja repetir a operação? 1.SIM 2.NÃO ' ))
if replay == 2:
    print('FIM')


    


