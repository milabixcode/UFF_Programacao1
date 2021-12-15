n = int(input())
m = int(input())
soma = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        iAoQuadrado = i**2
        iAoQuadradoVezesJ = iAoQuadrado*j
        tresElevadoAI = 3**i
        jVezesTresElevadoAI = j*(tresElevadoAI)
        iVezesTresElevadoAJ = i*(3**j)
        somaDiv = jVezesTresElevadoAI + iVezesTresElevadoAJ
        multDiv = tresElevadoAI * somaDiv

        soma = soma + (iAoQuadradoVezesJ/multDiv)
    
print("%.4f" %soma) 