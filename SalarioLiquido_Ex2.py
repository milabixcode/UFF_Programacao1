salarioBruto = int(input())

if(salarioBruto >= 500 and salarioBruto <= 800):
    salarioLiquido = salarioBruto * 0.9
    print("%.2f" %salarioLiquido)
elif(salarioBruto >= 800 and salarioBruto < 1000):
    salarioLiquido = salarioBruto * 0.75
    print("%.2f" %salarioLiquido)
elif(salarioBruto >= 1000):
    salarioLiquido = salarioBruto * 0.2
    print("%.2f" %salarioLiquido)
else:
    print("%.2f" %salarioBruto)
