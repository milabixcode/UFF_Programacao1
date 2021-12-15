numeroParticipantes, orcamento, numeroHoteis, numeroSemanas = map(int, input().split()) 

custoMinimo = None

for i in range(numeroHoteis):
    precoPorPessoa = int(input())
    camasDisponiveis = [0]*numeroSemanas
    camasDisponiveis = list(map(int, input().split()))
    custoDiarias = precoPorPessoa * numeroParticipantes
    camasSuficientes = True
    if custoDiarias <= orcamento:
        for j in range(numeroSemanas):        
            if camasDisponiveis[j] >= numeroParticipantes:
                if custoDiarias <= orcamento:
                    if custoMinimo != None:
                        if custoMinimo > custoDiarias:
                            custoMinimo = custoDiarias
                    else:
                        custoMinimo = custoDiarias
               
if custoMinimo:
    print(custoMinimo)
else:    
    print("stay home")

