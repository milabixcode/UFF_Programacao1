#n inteiro informado pelo usuário
n = int(input("n = "))
#variável acumuladora que vai começar em 1 pq é multiplicação
f = 1
#laço que tenho que multiplicar todos os números de f que começa em 1 até n + 1 ( pq o laço 
# roda estritamente até quando for menor que n+1, (no caso n). A cada interação do laço o f recebe o f
# multiplicado por i.
for i in range (1, n + 1, 1):
    f = f * i
print("fatorial de ",n, "=" ,f)