numero = int(input())
produto = 1
for i in range (1, 1000):
        produto = int(i * (i+1) * (i+2)) 
        if(numero == produto):
                print(i)
                print(i+1)
                print(i+2)
                break
if(numero != produto):
        print("não")
