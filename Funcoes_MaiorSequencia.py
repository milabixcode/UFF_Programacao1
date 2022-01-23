"""Escreva um programa que receba uma lista de N números inteiros e retorne, para o usuário, o
comprimento da maior sequência decrescente.
Exemplo:
Na lista [6, 9, 10, 8, 5, 3, 3, 4, 11], o comprimento da maior sequência decrescente é 4 (pois
10, 8, 5, 3 é a maior sequência decrescente). Já nesta lista [3, 4, 6, 6, 9, 11], o comprimento da
maior sequência é 1.
O programa deve ser implementado usando uma função que recebe apenas uma lista (vetor) e
retorna o tamanho da maior sequência decrescente encontrada para ser impressa."""

def getTamanhoMaiorSequencia(vetor):
    maiorSequenciaDeTodas = 1
    tamanhoSequenciaControle = 1
    for i in range (len(vetor) - 1):
        if vetor[i] > vetor[i+1]:
            tamanhoSequenciaControle += 1
        else:
            if tamanhoSequenciaControle > maiorSequenciaDeTodas:
                maiorSequenciaDeTodas = tamanhoSequenciaControle
                tamanhoSequenciaControle = 1
    return maiorSequenciaDeTodas

n = int(input())
lista = []
for i in range(n):
    lista.append(int(input()))
tamanho = getTamanhoMaiorSequencia(lista)
print(tamanho)
    