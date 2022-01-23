"""Todo fã de Dragon Ball conhece o famoso ataque do personagem Tenshinhan, o KIKOHO. Recentemente Tenshi, 
para os íntimos, foi batalhar com o guerreiro Cell. Foi uma batalha épica, ele conseguiu acertar alguns 
ataques em Cell, mas infelizmente ele não o venceu. Porém ficou satisfeito com a área total que seu 
ataque cobriu. Vamos aderir que o ataque de Tenshi é basicamente um triângulo, ele não sabe qual é a área
que esse ataque chegou a ter, mas ele sabe em quais pontos se encontram os vértices do triângulo formado.
Você pode ajudar Tenshi informando qual a área total que o seu ataque teve?"""

def calculate3x3MatrixDet(matrix):
    verticaisPrincipais = (matrix[0][0] * matrix[1][1] * matrix[2][2]) + (matrix[0][1] * matrix[1][2] * matrix[2][3]) + (matrix[0][2] * matrix[1][3] * matrix[2][4])
    verticaisSecundarias = (matrix[0][4] * matrix[1][3] * matrix[2][2]) + (matrix[0][3] * matrix[1][2] * matrix[2][1]) + (matrix[0][2] * matrix[1][1] * matrix[2][0])
    return abs(verticaisPrincipais - verticaisSecundarias)

testCase = int(input())
for i in range(testCase):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    A = [
        [x1, y1, 1, x1, y1],
        [x2, y2, 1, x2, y2],
        [x3, y3, 1, x3, y3]
    ]
    area = calculate3x3MatrixDet(A)/2
    print("{0:.3f}".format(area))