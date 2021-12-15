numeroDeIteracoes = int(input())
ordemCrescente = True
numeroAnterior = int(input())

for i in range(1,numeroDeIteracoes):
    numeroAtual = int(input())
    if numeroAnterior > numeroAtual:
        ordemCrescente = False
    numeroAnterior = numeroAtual
if ordemCrescente:
    print("sim")
else:
    print("não")
    



