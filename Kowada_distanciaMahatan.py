xa, ya, xb, yb = input().split()
variacaoX = (abs(int(xb) - int(xa))) 
variacaoY = (abs(int(yb) - int(ya)))
distancia = variacaoX + variacaoY
print(distancia)