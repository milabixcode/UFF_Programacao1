"""Uma locadora de videogame tem guardada, em uma lista de 10 posições, a quantidade de
jogos retirados por seus clientes durante o ano passado (i.e. Clientes[i] = X -> o cliente “i”
retirou X jogos no ano passado). Agora esta locadora está fazendo uma promoção e, para cada
5 jogos retirados no ano passado, o cliente tem direito a uma locação grátis. Faça um
programa que crie um outro vetor contendo a quantidade de locações gratuitas a que cada
cliente tem direito.
ENTRADA: 10 números inteiros (>=0) indicando o número de locações de cada cliente
SAIDA: vetor de inteiros indicando o número de locações gratuitas de cada cliente"""

numero = 10
listaJogosPorCliente = [0]*numero
listaLocacoesGratuitas = [0]*numero
indice = 0

for i in range(numero):
     listaJogosPorCliente[i] = int(input())

for i in range(numero):
    listaLocacoesGratuitas[indice] = int(listaJogosPorCliente[i]/5)
    indice = indice + 1

   
print(listaLocacoesGratuitas)
