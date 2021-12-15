n = int(input())
soma = int(input())
produto = soma
maiorNumero = soma
menorNumero = soma
for i in range(n-1):
    numeroAtual = int(input())
    soma = soma + numeroAtual
    produto = produto * numeroAtual
    if numeroAtual < menorNumero:
        menorNumero = numeroAtual
    elif numeroAtual > maiorNumero:
        maiorNumero = numeroAtual
    
media = float(soma/n)

print("%.2f" %media)
print(soma)
print(produto)
print(menorNumero)
print(maiorNumero)
