n = int(input())
contador = 0
while n != 0:
    x = -10000
    y = 10000
    u = 10000 
    v = -10000
contador += 1
for i in range(n):
    a, b, c, d = map(int, input().split())
    if a > x:
        x = a
    if b < y:
        y = b
    if c < u:
        u = c
    if d > v:
        v = d

if u > x or v > u:
    print('Teste', contador)
    print('nenhum')
    print()
else:
    print('Teste', contador)
    print(x, y, u, v)
    print()

    

"""3
0 6 8 1
1 5 6 3
2 4 9 0
3
0 4 4 0
3 1 7 -3
6 4 10 0
0"""
    
