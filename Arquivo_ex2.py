arquivo1 = open('nomes.txt', 'r')
arquivo2 = open('salarios.txt', 'r')
arquivo3 = open('folha.txt', 'w')

linha1 = arquivo1.readline()
linha2 = arquivo2.readline()

total = 0
#Condição de parada pode ser arquivo1 ou arquivo2 pq tem o mesmo num de elem
while (linha1 != ''):
    #quebrando arquivo sem parâmetro: ['willie','coiote']
    nome, sobrenome = linha1.split()
    # pode fazer direto pq so tem um valor
    salario = float(linha2)
    if (sobrenome != "Acme"):
        arquivo3.write(nome + '' + sobrenome + '' + str(salario) + '/n')
        total = total + salario
    linha1 = arquivo1.readline()
    linha2 = arquivo2.readline()

print('folha =', total)

arquivo1.close()
arquivo2.close()
arquivo3.close()
