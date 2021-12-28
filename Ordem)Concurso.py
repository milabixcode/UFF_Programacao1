"""Escreva um programa que:
(a) O usuário fornecerá o número de candidatos N, a matrícula e a nota de cada
candidato. O programa deve armazenar a matrícula dos candidatos em uma lista e a nota em
outra lista.
(b) Apresentar um relatório apresentando a matrícula do candidato em ordem crescente
de classificação de acordo com a nota obtida, como exemplo abaixo"""

numeroDeCandidatos = int(input())
matriculas = [0] * numeroDeCandidatos
notaCandidato = [0] * numeroDeCandidatos

for i in range(numeroDeCandidatos):
    matriculas[i] = int(input())
for i in range(numeroDeCandidatos):
    notaCandidato[i] = float(input())

for i in range(numeroDeCandidatos):
    for j in range(numeroDeCandidatos-1):
        if notaCandidato[j] > notaCandidato[j+1]:
            notaCandidato[j], notaCandidato[j+1] = notaCandidato[j+1], notaCandidato[j]
            matriculas[j], matriculas[j+1] = matriculas[j+1], matriculas[j]

print(matriculas)