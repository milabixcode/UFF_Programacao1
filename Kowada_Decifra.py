alfabetoCriptografado = {}
alfabeto = list(map(str,"a b c d e f g h i j k l m n o p q r s t u v w x y z".split()))
permutacao = list(input())
fraseCriptografada = list(input())
fraseDecriptografada = ""

for i in range(26):
    alfabetoCriptografado[permutacao[i]] = alfabeto[i]

for i in range(len(fraseCriptografada)):
    fraseDecriptografada += alfabetoCriptografado[fraseCriptografada[i]]

print(fraseDecriptografada)

