x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

x2MenosX1AoQuadrado = (x2 - x1)**2
y2MenosY1AoQuadrado = (y2 - y1)**2

distancia = (x2MenosX1AoQuadrado + y2MenosY1AoQuadrado)**0.5

print("d = %.2f" % distancia)