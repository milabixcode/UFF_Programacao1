x = int(input())
elemento1 = 0
elemento2 = 1
elemento3 = elemento1 + elemento2
if(x == 1):
    print(elemento1)
elif(x== 2):
    print(elemento1)
    print(elemento2)
else:

    print(elemento1)
    print(elemento2)

    for i in range(x-2):
        elemento3 = elemento1 + elemento2
        elemento1 = elemento2
        elemento2 = elemento3
        print(elemento3)
    