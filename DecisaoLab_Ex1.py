valor1 = int(input())
valor2 = int(input())
valor3 = int(input())

if(valor1 == valor2 == valor3):
    print("iguais")
elif(valor1 == valor2):
    soma1 = (valor1 + valor2) - valor3
    print(soma1)
elif(valor1 == valor3):
    soma2 = (valor1 + valor3) - valor2
    print(soma2)
elif(valor2 == valor3):
    soma3 = (valor2 + valor3) - valor1
    print(soma3)
elif(valor1 > valor2 and valor1 > valor3 and valor2 > valor3):
    print(valor1, valor2, valor3)
elif(valor1 > valor2 and valor1 > valor3 and valor3 > valor2):    
    print(valor1, valor3, valor2)
elif(valor2 > valor1 and valor2 > valor3 and valor1 > valor3):
    print(valor2, valor1, valor3)
elif(valor2 > valor1 and valor2 > valor3 and valor3 > valor1):
    print(valor2, valor3, valor1)
elif(valor3 > valor1 and valor3 > valor2 and valor1 > valor2):
    print(valor3, valor1, valor2)    
else:
    print(valor3, valor2, valor1)
 