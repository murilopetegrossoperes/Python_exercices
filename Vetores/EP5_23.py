#você deve calcular a distância entre dois pontos localizados em um espaço tridimensional. Cada ponto será representado por um vetor de 3 elementos reais, correspondendo às coordenadas x, y e z.
n = 3
cordenada_x1_y1_z1 = input().split(" ")
cordenada_x2_y2_z2 = input().split(" ")
v1 = [0] * n
v2 = [0] * n

for i in range(n):
    v1[i] = float(cordenada_x1_y1_z1[i])

for i in range(n):
    v2[i] = float(cordenada_x2_y2_z2[i])

x1= float(cordenada_x1_y1_z1[0])
y1= float(cordenada_x1_y1_z1[1])
z1= float(cordenada_x1_y1_z1[2])

x2= float(cordenada_x2_y2_z2[0])
y2= float(cordenada_x2_y2_z2[1])
z2= float(cordenada_x2_y2_z2[2])

d = (((x2-x1)**2)+((y1-y2)**2)+((z1-z2)**2))**0.5
print(f"A distancia entre os dois pontos eh {d:.2f}.")