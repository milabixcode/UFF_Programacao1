import random

numero1 = random.randint(0,6)
numero2 = random.randint(0,6)
numero3 = random.randint(0,6)

if(numero2 == numero1 + 1 and numero3 == numero2 + 1):
    soma = numero1 + numero2 + numero3
    print(soma)
elif(numero1 != numero2 != numero3):
    print("não deu")
elif(numero1 == numero2):
    multiplicacao = numero1 * numero2
    print(multiplicacao)
elif(numero1 == numero3):
    multiplicacao = numero1 * numero3
    print(multiplicacao)
else:
    multiplicacao = numero2 * numero3
    print(multiplicacao)
