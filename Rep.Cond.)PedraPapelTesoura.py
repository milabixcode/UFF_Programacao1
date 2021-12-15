pedra = 0
spock = 1
paper = 2
lagarto = 3
tesoura = 4

vitoria1 = 0
vitoria2 = 0
empate = 0

for i in range(3):
    jogador1 = int(input())
    jogador2 = int(input())
    if jogador1 == 0 and (jogador2 == 3 or jogador2 == 4):
        vitoria1 = vitoria1 + 1
    elif jogador1 == 1 and (jogador2 == 4 or jogador2 == 0):
        vitoria1 = vitoria1 + 1
    elif jogador1 == 2 and (jogador2 == 1 or jogador2 == 0):
        vitoria1 = vitoria1 + 1
    elif jogador1 == 3 and (jogador2 == 1 or jogador2 == 2):
        vitoria1 = vitoria1 + 1
    elif jogador1 == 4 and (jogador2 == 2 or jogador2 == 3):
        vitoria1 = vitoria1 + 1
    elif jogador1 == jogador2:
        empate = empate + 1
    else:
        vitoria2 = vitoria2 + 1

print(vitoria1)
print(vitoria2)
print(empate)