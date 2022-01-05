n = int(input())
contador = 0
while n != 0:
    a = -10000
    c = 10000
    b = -10000
    d = 10000
    for i in range(n):
        x,y,u,v = map(int,input().split())
        if x > a:
            a = x
        if y < c:
            c = y
        if u < d:
            d = u
        if v > b:
            b = v
    contador += 1
    print("Teste", contador)
    if a < d and b < c:
       print(a, c, d, b)
       print()
    else:
        print("nenhum")
        print()
    n = int(input())
