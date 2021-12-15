#Faça um programa que imprima os N (inteiro fornecido pelo usuário) primeiros números da série de Yoshi. 
#A série inicia com os números 2,5 e 8, e cada número posterior equivale a diferença entre o número anterior 
#e a soma dos 2 números antes do anterior (ex: o próximo número da série é 8-(2+5)=1). No fim, pergunte se o 
#usuário quer entrar com outro N e repetir o processo.
opcao = 1
while opcao == 1:
    N = int(input())
    numero1 = 2
    numero2 = 5
    numero3 = 8
    numeroPosterior = numero3 - (numero1 + numero2)
    print(numero1)
    print(numero2)
    print(numero3)
    print(numeroPosterior)

    for i in range(0, N-4, 1):
        numero1 = numero2
        numero2 = numero3
        numero3 = numeroPosterior
        numeroPosterior = numero3 - (numero1 + numero2)
        print(numeroPosterior)

    print("Quer receber outro n?")
    print("1 - Sim  2 - Não")
    opcao = int(input())

print("Game Over")

