# o seu programa deve capturar uma sequência de seis valores inteiros e exibi-los na tela exatamente na ordem contrária à que foram inseridos.
n = 6
v = [0] * n
itens_linha = input().split(" ")
for i in range(n):
    v[i] = int(itens_linha[i])

i=0
for i in range(n//2):
    temp = v[i]
    
    v[i] = v[(n - 1) - i]
    

    v[(n - 1) - i] = temp
for i in range(n):
  print(v[i], end=" ")
