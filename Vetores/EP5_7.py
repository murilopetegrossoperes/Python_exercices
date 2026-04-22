#seu desafio é verificar se um vetor possui simetria perfeita, ou seja, se a sua primeira metade é exatamente o inverso da segunda metade.

n = int(input())
cont = 0
v=[0]*n

for i in range(n):
  v[i] = [int(input())]
i = 0
while i < n//2:
    if v[0+i] == v[n-(1)-i]:
      i += 1
      cont += 1
    else:
      i += 1
if cont == n//2:
  print("SIM")
else:
  print("NAO")
