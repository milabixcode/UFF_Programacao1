"""Prova Kowada
def criaVetor(fill, n):
    return [fill] * n

def criaMatrix(fill, m, n):
    matrix = [[]] * m
    for i in range(m):
        matrix[i] = [fill] * n

    return matrix

def estabeleceAresta(arestas, de, para):
    arestas[de][para] = True
    arestas[para][de] = True

def enfilera(fila, vertice):
    fila.append(vertice)

def visita(visitados, vertice):
    visitados[vertice] = True

def quebraStringEmInteirosNumVetor(string):
    return [int(i) for i in string.split() if i.isdigit()]

def enfileiraVizinhos(enfileirados, arestas, vertice):
    for i in range(len(arestas[vertice])):
        if arestas[vertice][i]:
            enfileirados.append(i)

def normalizaAresta(aresta):
    aresta[0] = aresta[0] -1
    aresta[1] = aresta[1] -1

NL = quebraStringEmInteirosNumVetor(input())

arestas = criaMatrix(False, NL[0], NL[0])
visitados = criaVetor(False, NL[0])
enfileirados = []

primeiraAresta = quebraStringEmInteirosNumVetor(input())
normalizaAresta(primeiraAresta)
enfilera(enfileirados, primeiraAresta[0])
estabeleceAresta(arestas, primeiraAresta[0], primeiraAresta[1])

for i in range(NL[1] -1):
    aresta = quebraStringEmInteirosNumVetor(input())
    normalizaAresta(aresta)
    estabeleceAresta(arestas, aresta[0], aresta[1])

while(len(enfileirados) != 0):
    vertice = enfileirados.pop(0)
    if(not visitados[vertice]):
        visitados[vertice] = True
        enfileiraVizinhos(enfileirados, arestas, vertice)

isCompleto = True

for visitado in visitados:
    isCompleto &= visitado

if isCompleto:
    print("COMPLETO")
else:
    print("INCOMPLETO")"""

n, l = map(int, input().split()) 
p=True 
fila = [] 
fila.append(1) 
visitados = [False]*n 
matriz = [[]] * n 
for i in range(len(matriz)):   
    matriz[i] = [False] * n  
    for j in range(l):     
        vertice1, vertice2 = map(int, input().split())     
        matriz[vertice1-1][vertice2-1] = True     
        matriz[vertice2-1][vertice1-1] = True  
while len(fila) !=0:     
    x = fila.pop(0)     
if not visitados[x]:         
    visitados[x] = True         
for i in range(n):             
    if matriz[x][i]:                 
        fila.append(i) 
        for i in visitados:      
            p = p and i 
            if not p:     
                print("INCOMPLETO") 
            else:     
                print(("COMPLETO"))
