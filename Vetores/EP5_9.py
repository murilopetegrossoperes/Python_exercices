#Nesta atividade, você deve verificar se dois vetores A e B são proporcionais. Ou seja, se o vetor B é o resultado da multiplicação de todos os elementos de A por uma mesma constante escalar.

n = int(input())
v1 = [0] * n
v2 = [0] * n
cont=0

itens_linha1 = input().split(" ")
for i in range(n):
  v1[i] = int(itens_linha1[i])

itens_linha2 = input().split(" ")
for i in range(n):
  v2[i] = int(itens_linha2[i])

i = 0
k = (v1[0] / v2[0])


while i < n:
  if (v1[i]/v2[i]) == k:
    i += 1
    cont += 1
  else:
    i += 1
if cont == n:
  print("SIM")
else:
  print("NAO")
