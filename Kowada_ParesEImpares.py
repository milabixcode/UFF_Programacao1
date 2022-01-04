"""Considerando a entrada de valores inteiros não negativos, ordene estes valores segundo o seguinte 
critério:
Primeiro os Pares
Depois os Ímpares
Sendo que deverão ser apresentados os pares em ordem crescente e depois os ímpares em ordem decrescente.
Entrada
A primeira linha de entrada contém um único inteiro positivo N (1 < N <= 105) Este é o número de linhas 
de entrada que vem logo a seguir. As próximas N linhas conterão, cada uma delas, um valor inteiro não 
negativo.
Saída
Apresente todos os valores lidos na entrada segundo a ordem apresentada acima. Cada número deve ser 
impresso em uma linha, conforme exemplo abaixo."""

n = int(input())
vetor = [0] *n

for i in range(n):
    vetor[i] = int(input())

vetor.sort()

vetorPares = []
vetorImpares = []

for i in range(n):
    if vetor[i] % 2 == 0 or vetor[i] == 0:
        print(vetor[i])
    else:
        vetorImpares.append(vetor[i])

vetorImparesDecrescente = []
for i in range(len(vetorImpares)-1, -1, -1):
    vetorImparesDecrescente.append(vetorImpares[i])
    print(vetorImpares[i])


