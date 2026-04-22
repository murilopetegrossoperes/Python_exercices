#seu programa deve atuar como um filtro de vizinhança. O objetivo é percorrer um vetor de n elementos e somar todos os valores que estejam posicionados ao lado de qualquer elemento que possua o valor 1.

n = int(input())
i= 0
soma=0
v=[0]*n

for i in range(n):
  v[i] = int(input())

for i in range(n):
  if v[i] == 1:

    val_ant = v[i-1] if i > 0 else 0 
 
    val_prox = v[i+1] if i < n - 1 else 0 
    
    if i > 0: 
        soma += v[i-1]
    if i < n - 1: 
        soma += v[i+1]



print(soma)