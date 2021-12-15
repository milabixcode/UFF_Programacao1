#*Faça um programa que calcula os primeiros X números da Santa série de Seiya (X inteiro
#positivo fornecido pelo usuário). A série santificada de Seiya inicia com os números 1 e 2, e cada número posterior 
#equivale à multiplicação dos dois números anteriores, mais 1. Por exemplo, caso o usuário informe X=6, o resultado 
#seria: 1, 2, 3, 7, 22, 155. No final, receba mais um inteiro R para informar se o usuário quer repetir o processo
#(onde R será 1-sim, 2-não).
#ENTRADA: um número par de inteiros indicando o número de elementos da série impressos
#(X>=1) e o inteiro indicando se o processo será repetido (R=1 ou R=2)
#SAIDA: número(s) (inteiros), um por linha, indicando a(s) saída(s) da(s) série(s).
opcao = 1
while opcao == 1:
    x = int(input())
    numero1 = 1
    numero2 = 2
    if(x == 1):
        print(numero1)
    elif(x == 2):
        print(numero1)
        print(numero2)
    else:
        print(numero1)
        print(numero2)
        
        for i in range(x-2):
            numeroPosterior = (numero1*numero2) + 1
            numero1 = numero2
            numero2 = numeroPosterior
            
            print(numeroPosterior)

    opcao = int(input())


