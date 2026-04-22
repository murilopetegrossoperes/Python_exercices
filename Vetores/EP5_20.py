#você deve implementar uma funcionalidade para trocar as posições de dois valores dentro de um vetor. O programa lerá o tamanho n, os elementos do vetor e, por fim, dois índices i e j que indicam quais elementos devem mudar de lugar.
n = int(input())
itens_linha1 = input().split(" ")
v1=[0]*n
v2=[0]*n

for i in range(n):
    v1[i] = (itens_linha1[i])

i = int(input())
j = int(input())

if 0 <= i and i < n and 0 <= j and j < n:
  v2 = v1[i]
  v1[i] = v1[j]
  v1[j] = v2
print(v1)