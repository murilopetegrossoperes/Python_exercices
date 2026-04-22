#o objetivo é manipular a estrutura de um vetor para remover um elemento em um índice específico. Como o tamanho do vetor é fixo, a "remoção" é feita deslocando os elementos subsequentes para a esquerda e preenchendo a última posição com o valor -1.
n = int(input())
itens_linha = input().split(" ")
i_removido = int(input())
i= 0
v=[0]*n

for i in range(n):
    v[i] = int(itens_linha[i])

for i in range(n):
  print(v[i], end=" ")
print()

for i in range(i_removido, n-1):
  v[i] = v[i+1]
v[n-1] = -1

for i in range(n):
  print(v[i], end=" ")