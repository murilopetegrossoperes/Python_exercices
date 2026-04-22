#Neste exercício, seu programa deve identificar se uma sequência de números inteiros está organizada em ordem crescente.

cont_positivo = 0
cont_negativo = 0
n = int(input())
v = [0] * n

itens_linha = input().split(" ")
for i in range(n):
  v[i] = int(itens_linha[i])

i=0
while i < n-1:
    if v[i] <= v[i+1]:
      i += 1
      cont_positivo += 1
    else:
      i += 1
      cont_negativo += 1

if cont_positivo == i:
  print("SIM")
elif cont_negativo == i:
    print("NAO")
else:
    print("NAO")