casosDeTeste = int(input())

for i in range(casosDeTeste):
    numeroDeInstrucoes = int(input())
    memoriaDeInstrucoes = [0]*numeroDeInstrucoes
    for j in range(numeroDeInstrucoes):
        instrucao = input()
        if(instrucao == "LEFT"):
            memoriaDeInstrucoes[j] = -1
        elif(instrucao == "RIGHT"):
            memoriaDeInstrucoes[j] = 1
        else:
            posicao = 0
            for k in instrucao.split(): 
                if k.isdigit():
                    posicao = int(k)

            memoriaDeInstrucoes[j] = memoriaDeInstrucoes[posicao - 1]
    p = 0
    for m in range(numeroDeInstrucoes):
        p += memoriaDeInstrucoes[m]

    print(p)