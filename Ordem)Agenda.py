"""Agenda
Faça um programa que simule uma agenda telefônica onde o usuário informe os telefones
(inteiros) e você deverá inserir estes valores numa lista, onde ela se mantem ordenada de
forma crescente. A cada número inserido, imprima a agenda."""

n = int(input())
listaFinal = []

for i in range (n):        
    elemento = int(input())
    listaFinal.append(elemento)
    for k in range(len(listaFinal)):        
        for j in range(1, len(listaFinal)):
                if listaFinal[j-1] > listaFinal[j]:
                    listaFinal[j-1], listaFinal[j] = listaFinal[j], listaFinal[j-1]
    print(listaFinal)
            

