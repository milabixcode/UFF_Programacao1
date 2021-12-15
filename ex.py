NLString = input()
NL = NLString.split()
NLInt = []

for i in range(len(NL)):
    NLInt.append(int(NL[i]))
segmentosConectados = [False]*NLInt[0]
XYString = input()
XY = XYString.split()
XYInt = []
for j in range(len(XY)):
    XYInt.append(int(XY[j]))
segmentosConectados[XYInt[0] - 1] = True
segmentosConectados[XYInt[1] - 1] = True
for i in range(NLInt[1]-1):
    XYString = input()
    XY = XYString.split()
    XYInt = []
    for j in range(len(XY)):
        XYInt.append(int(XY[j]))
    segmentosConectados[XYInt[1] - 1] = True
estaCompleto = True
for i in range(len(segmentosConectados)):
    if segmentosConectados[i] == False:
        estaCompleto = False   
if estaCompleto == True:
    print("COMPLETO") 
else:
    print("INCOMPLETO")