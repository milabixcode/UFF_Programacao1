for i in range(100,1000):
    algarismo1 = int(i/100)
    algarismo2 = int((i - algarismo1*100)/10) 
    algarismo3 = int(i - algarismo1*100 - algarismo2*10)   
    produto = int(algarismo1**3 + algarismo2**3 + algarismo3**3) 
    if( i == produto ):
       print(produto)
