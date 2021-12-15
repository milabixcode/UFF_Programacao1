"""Faça um programa que receba um conjunto de 10 elementos numéricos e os armazene em
uma lista (vetor). Em seguida, o programa deverá procurar se existem no vetor elementos
iguais a um dado valor também informado pelo usuário e imprimir o índice das posições em
que estes são encontrados.
ENTRADA: 10 números inteiros e mais um número inteiro indicando o número a ser procurado
SAIDA: vetor de inteiros indicando as posições em que o número foi encontrado no vetor."""

"""inicializo uma variável para contar quantos índices minha lista de resultados terá"""
indices = 0
"""inicializo uma variável para contar quantos números iguais minha lista de resultados terá"""
numeroIgual = 0
"""Quantidade de elementos da minha lista de elementos numéricos"""
numeros = 10
"""Quantos elementos serão adicionados a minha lista """
elementosNumericos = [0]*numeros

"""Adiciono os itens da minha lista"""
for i in range(0,numeros):
    elementosNumericos[i] = int(input())   

"""escolho meu numero que será comparado"""
numeroEscolhido = int(input())

"""atualizo quantos numeros iguais minha lista tem """
for i in range(0,numeros):
    if elementosNumericos[i] == numeroEscolhido:
        numeroIgual = numeroIgual + 1

"""Quantidade de itens que minha lista vai percorrer"""
listaResultados = [0]*numeroIgual

"""atualizo minha quantidade de indices"""
for i in range(0,numeros):
    if elementosNumericos[i] == numeroEscolhido:
        listaResultados[indices] = i
        indices = indices + 1

print(listaResultados)     
