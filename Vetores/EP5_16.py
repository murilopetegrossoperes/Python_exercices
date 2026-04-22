#você deve realizar uma operação aritmética entre dois conjuntos de dados. O programa deve receber dois vetores, A e B, cada um com 5 números inteiros, e gerar um terceiro vetor C onde cada posição é o resultado de C[i]=A[i]−B[i].
n = 5
v1 = [0] * n
itens_linha1 = input().split(" ")
for i in range(n):
    v1[i] = int(itens_linha1[i])

v2 = [0] * n
itens_linha2 = input().split(" ")
for i in range(n):
    v2[i] = int(itens_linha2[i])

v3 = [0] * n
for i in range(n):
    v3[i] = v1[i] - v2[i]

for i in range(n):
  print(v3[i], end=" ")