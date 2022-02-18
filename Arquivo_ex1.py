arquivo = open('arquivo.txt', 'r')

for linha in arquivo:
    aluno, n1, n2, n3 = linha.split(",")
    media = (float(n1) + float(n2) + float(n3))/3
    if media >= 7:
        print(aluno, media)

arquivo.close()