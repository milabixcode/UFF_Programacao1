import math
jogadorA = int(input())
jogadorB = int(input())
n = 0

while (jogadorB > jogadorA):
    jogadorA = jogadorA + math.floor(0.5*jogadorA)
    jogadorB = jogadorB + math.floor(0.3*jogadorB)
    n = n + 1
print(n)