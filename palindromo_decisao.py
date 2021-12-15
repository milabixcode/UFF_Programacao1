import math

palindromo = int(input())
valor1 = math.floor(palindromo/10000)
valorInteiro = palindromo - (valor1*10000)
valor2 = math.floor((valorInteiro)/1000)
valorInteiro = valorInteiro-(valor2*1000)
valor3 = math.floor(valorInteiro/100)
valorInteiro = valorInteiro-(valor3*100)
valor4 = math.floor(valorInteiro/10)
valorInteiro = valorInteiro-(valor4*10)
valor5 = math.floor(valorInteiro)

if(valor1 == valor5 and valor2 == valor4):
    print("sim")
else:
    print("não")