numero1 = int(input())
numero2 = int(input())
numero3 = int(input())

if(numero1 == numero2 == numero3):
    print(0)
elif(numero1 == numero2):
    print(numero3)
elif(numero1 == numero3):
    print(numero2) 
elif(numero2 == numero3):
    print(numero1)
else:
    soma = numero1 + numero2 + numero3
    print(soma)
