#Uma empresa de logística precisa calcular a distância entre sua sede e diversos pontos de entrega. Você receberá as coordenadas da empresa (x,y) e um vetor contendo pares de coordenadas para n entregas no formato [x1,y1,x2,y2,…]
cordenada_x1 = int(input())
cordenada_y1 = int(input())
n = int(input())
itens_linha = input().split(" ")
v = [0] * n

for i in range(n):
    v[i] = int(itens_linha[i])

for i in range(n):
  print(v[i], end=" ")
print()

x1= int(cordenada_x1)
y1= int(cordenada_y1)

for i in range(n-1): 
  if i % 2 == 0:
    x2 = v[i]
    y2 = v[i+1]
    d = (((x2-x1)**2)+((y2-y1)**2))**0.5
    print(f"{d:.2f}", end=" ")
