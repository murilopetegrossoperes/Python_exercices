#você deve verificar a organização dos elementos dentro de um vetor. Um "vetor de duplas" é aquele onde todos os elementos estão organizados em pares idênticos e em posições consecutivas.

n = int(input())
i= 0
v=[i]*(n)

for i in range(n):
  v[i] = int(input())
if n%2==1:
  print("Nao eh um vetor de duplas!")
elif v[i] == v[(i-1)]:
  print("Eh um vetor de duplas!")
else:
  print("Nao eh um vetor de duplas!")