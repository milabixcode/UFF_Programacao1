x = int(input())
numero = 3
denominador = 7
soma = x + (numero*x)/denominador
for i in range(49):
    numero = numero + 5
    numerador = numero*x
    denominador = denominador + 2
    soma = soma - numerador/denominador
    numero = numero + 5
    numerador2 = numero*x
    denominador = denominador + 2
    soma = soma + numerador2/denominador
print("%.3f" %soma)
   

    