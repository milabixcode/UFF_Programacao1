def getMaiorNumeroDaSequencia(h): 
    hNMenos1 = h
    maiorNumeroDaSequencia = hNMenos1
    while(hNMenos1 != 1):
        if hNMenos1 % 2 == 0:
            hNMenos1 = int(hNMenos1/2)
        else:
            hNMenos1 = (3 * hNMenos1) + 1
        if hNMenos1 > maiorNumeroDaSequencia:
            maiorNumeroDaSequencia = hNMenos1
    return maiorNumeroDaSequencia
    
h = int(input())
maiorDaSequencia = getMaiorNumeroDaSequencia(h)
print(maiorDaSequencia)