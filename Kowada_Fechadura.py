n, m = map(int,input().split())
pinos = list(map(int, input().split()))

count = 0
for i in range(n-1):
    while pinos[i] != m:
        if pinos[i] < m:
            pinos[i] += 1
            pinos[i+1] += 1
        else:
            pinos[i] -= 1
            pinos[i+1] -= 1
        count += 1

while pinos[-1] != m:
        if pinos[-1] < m:
            pinos[-1] += 1
        else:
            pinos[-1] -= 1
        count += 1

print(count)