x = int(input())
soma = 0
for i in range (x):
    nota1 = float(input())
    nota2 = float(input())
    media = (nota1 + nota2)/2
    soma = soma + media
print("%.2f" %soma)