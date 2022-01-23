"""Júlio César usava um sistema de criptografia, agora conhecido como Cifra de César, que trocava cada 
letra pelo equivalente em duas posições adiante no alfabeto (por exemplo, 'A' vira 'C', 'R' vira 'T', etc.).
Ao final do alfabeto nós voltamos para o começo, isto é 'Y' vira 'A'. Nós podemos, é claro, tentar trocar
as letras com quaisquer número de posições.
Entrada
A entrada contém vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a 
quantidade de casos de teste. Cada caso de teste é composto por duas linhas. A primeira linha contém uma 
string com até 50 caracteres maiúsculos ('A'-'Z'), que é a sentença após ela ter sido codificada através 
desta Cifra de César modificada. A segunda linha contém um número que varia de 0 a 25 e que representa 
quantas posições cada letra foi deslocada para a direita.
Saída
Para cada caso de teste de entrada, imprima uma linha de saída com o texto decodificado (transformado 
novamente para o texto original) conforme as regras acima e o exemplo abaixo."""

alphabet = ["Z","Y","X","W","V","U","T","S","R","Q","P","O","N","M","L","K","J","I","H","G","F","E","D","C","B","A"]
alphabet = ["Z","Y","X","W","V","U","T","S","R","Q","P","O","N","M","L","K","J","I","H","G","F","E","D","C","B","A"]
mapAlphabet = {
"A":25,
"B":24,
"C":23,
"D":22,
"E":21,
"F":20,
"G":19,
"H":18,
"I":17,
"J":16,
"K":15,
"L":14,
"M":13,
"N":12,
"O":11,
"P":10,
"Q":9,
"R":8,
"S":7,
"T":6,
"U":5,
"V":4,
"W":3,
"X":2,
"Y":1,
"Z":0
}
numberOfTestCases = int(input())
for i in range(numberOfTestCases):
    cipher = input()
    positionToRight = int(input())
    decipher = ""
    for letter in cipher:
        newPosition = (mapAlphabet[letter] + positionToRight) % 26
        decipher += alphabet[newPosition]
    print(decipher)