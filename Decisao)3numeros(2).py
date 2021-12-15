numero1 = int(input())
numero2 = int(input())
numero3 = int(input())


if(numero1 + numero2 == numero3 or numero2 + numero3 == numero1 or numero1 + numero3 == numero2):
    print("soma")
elif(numero1 * numero2 == numero3 or numero2 * numero3 == numero1 or numero1 * numero3 == numero2):
    print("multi")
else:
    soma = numero1 + numero2 + numero3
    if(soma %2 == 0):
        print("par")
    else:
        print("ímpar")