"""Crie uma função para calcular e armazenar numa lista (vetor) os n primeiros números de
Tribonacci. A série de Tribonacci consiste em:
1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504,...
Para calcula-la o primeiro elemento vale 1, o segundo elemento vale 1, o terceiro elemento vale
2, e daí por diante. Assim, o i-ésimo elemento vale o (i-1)-ésimo elemento somado ao (i-2)-
ésimo elemento somado ao (i-3)-ésimo elemento. Exemplo, 13=7+4+2.
O programa deve ser implementado usando uma função que recebe apenas um inteiro N e
uma lista (vetor) de tamanho N composta por 0s e retorna a lista preenchida com os N
primeiros elementos da série de Tribonacci para ser impressa."""

def preencheTribonacci(n, lista):
    if n == 1:
        lista[0] = 1
    elif n == 2:
        lista[0] = 1
        lista[1] = 1
    elif n == 3:
        lista[0] = 1
        lista[1] = 1
        lista[2] = 2
    else:
        lista[0] = 1
        lista[1] = 1
        lista[2] = 2
        for i in range(3, n, 1):
            lista[i] = lista[i-1] + lista[i-2] + lista[i-3]

n = int(input())
vetor = [0]*n
preencheTribonacci(n, vetor)
print(vetor)