valor1 = int(input())
valor2 = int(input())
valor3 = int(input())

media = (valor1 + valor2 + valor3)/3
soma = valor1 + valor2 + valor3
produto = valor1 * valor2 * valor3
print("%.1f" %media)
print(soma)
print(produto)
if(valor1 <= valor2 <= valor3):
    print(valor1)
    print(valor3)
elif(valor1 <= valor3 <= valor2):
    print(valor1)
    print(valor2)
elif(valor2 <= valor1 <= valor3):
    print(valor2)
    print(valor3)
elif(valor2 <= valor3 <= valor1):
    print(valor2)
    print(valor1)
elif(valor3 <= valor2 <= valor1):
    print(valor3)
    print(valor1)
else:
    print(valor3)
    print(valor2)