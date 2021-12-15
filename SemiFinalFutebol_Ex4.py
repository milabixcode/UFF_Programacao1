import random
import math

timeA = input()
timeB = input()
timeC = input()
timeD = input()

mediaGolsTimeA = math.ceil(float(input()))
mediaGolsTimeB = math.ceil(float(input()))
mediaGolsTimeC = math.ceil(float(input()))
mediaGolsTimeD = math.ceil(float(input()))

golsSemifinalTimeA = random.randint(0, mediaGolsTimeA) 
golsSemifinalTimeB = random.randint(0, mediaGolsTimeB)
print("Semifinal 1")
print(timeA, golsSemifinalTimeA, "x", golsSemifinalTimeB, timeB) 
if(golsSemifinalTimeA > golsSemifinalTimeB):
    finalista1 = timeA
    mediaGolsFinalista1 = golsSemifinalTimeA
elif(golsSemifinalTimeB > golsSemifinalTimeA):
    finalista1 = timeB
    mediaGolsFinalista1 = golsSemifinalTimeB
else:
    finalista1 = timeA
    mediaGolsFinalista1 = golsSemifinalTimeA
print(finalista1, "se classificou")

golsSemifinalTimeC = random.randint(0, mediaGolsTimeC) 
golsSemifinalTimeD = random.randint(0, mediaGolsTimeD) 
print("Semifinal 2")
print(timeC, golsSemifinalTimeC, "x", golsSemifinalTimeD, timeD) 
if(golsSemifinalTimeC > golsSemifinalTimeD):
    finalista2 = timeC
    mediaGolsFinalista2 = golsSemifinalTimeC
elif(golsSemifinalTimeD > golsSemifinalTimeC):
    finalista2 = timeD
    mediaGolsFinalista2 = golsSemifinalTimeD
else:
    finalista2 = timeC
    mediaGolsFinalista2 = golsSemifinalTimeC
print(finalista2, "se classificou")

golsFinalista1 = random.randint(0, mediaGolsFinalista1) 
golsFinalista2 = random.randint(0, mediaGolsFinalista2)
print("Final")
print(finalista1, golsFinalista1, "x", golsFinalista2, finalista2) 

if(golsFinalista1 > golsFinalista2):
    print(finalista1, "CAMPEÃO")
elif(golsFinalista2 > golsFinalista1):
    print(finalista2, "CAMPEÃO")
elif(golsFinalista1 == golsFinalista2):
    penalidadesFinalista1 = random.randint(0,5)
    penalidadesFinalista2 = random.randint(0,5)
    if(penalidadesFinalista1 > penalidadesFinalista2):
        print(finalista1, "CAMPEÃO")
    elif(penalidadesFinalista2 > penalidadesFinalista1):
        print(finalista2, "CAMPEÃO")
    else:
        cara = finalista1
        coroa = finalista2 
        ladoMoeda = random.randint(1,100)
        if(ladoMoeda <= 50):
            print(finalista1, "CAMPEÃO")
        else:
            print(finalista2, "CAMPEÃO")
    

