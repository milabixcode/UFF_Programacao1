total = 0.0
c3 = 0
for j in range (1, 11, 1):
    salario = float(input("Salário ="))
    classe = int(input("Classe = "))
    nome = ""

    if classe == 1:
        salario = salario + salario
        nome = "bom"
    if classe == 2:
        salario == salario + (salario/2)
        nome = "medio"
    if classe == 3:
        salario == salario
        nome = "nhe"
        c3 = c3 + 1

    total = total + salario
    print("Salário = ", salario, "classe =",nome)
print("classe 3 =", c3,"Total = ", total)

#pq nao esta imprimindo o nome?