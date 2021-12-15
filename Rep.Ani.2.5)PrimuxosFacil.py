""" Faça um programa que receba dois inteiros A e B e imprima todos os números PRIMUXOS
entre os números A e B (incluindo A e B). Um número é pimuxo se ele for primo e a soma de
seus dígitos é um número par. Ex: 31 é um número primuxo já que é primo e 3+1=4 é par.
ENTRADA: números inteiros A e B onde 100<= A <= B <= 999 (Pode acreditar, veja que assim
todos os números analisados tem necessariamente 3 dígitos)
SAIDA: número(s) (inteiros), um por linha, indicando os números primuxos """

a = int(input())
b = int(input())

for i in range(a,b+1):
    primo = 0
    c = int(i/100)
    d = int((i - (100*c))/10)
    u = int((i-c*100)-d*10)
    for j in range(2,i):
        if(i%j == 0):
            primo = primo + 1
    if(primo == 0) and (i != 1) and ((c+d+u)%2==0):
        print(i)