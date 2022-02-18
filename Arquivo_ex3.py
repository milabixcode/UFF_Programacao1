#preciso abrir os arquivos de saída e de entrada
arquivo1 = open('ips.txt','r')
arquivo2 = open('validos.txt', 'w')
arquivo3 = open('invalidos.txt', 'w')

for linha1 in arquivo1:
    n1, n2, n3, n4 = linha1.split('.')
    print (n1, n2, n3, n4)

    if((int(n1) <= 255 and int(n1) >= 0)) and (int(n2) <= 255 and int(n2) >= 1) and (int(n3) <= 255 and int(n3) >= 1) and (int(n4) <= 255 and int(n4) >= 1):
      arquivo2.write(linha1)
    else:
        arquivo3.write(linha1)

arquivo1.close()
arquivo2.close()
arquivo3.close()