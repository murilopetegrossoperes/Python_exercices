# você deve calcular o produto escalar entre dois vetores x e y, cada um contendo 5 números reais. O produto escalar é a soma dos produtos dos elementos correspondentes de cada vetor.

n = 5
cordenada_x1_y1_z1 = input().split(" ")
cordenada_x2_y2_z2 = input().split(" ")
soma = 0 
v1 = [0] * n
v2 = [0] * n

for i in range(n):
    v1[i] = float(cordenada_x1_y1_z1[i])


for i in range(n):
    v2[i] = float(cordenada_x2_y2_z2[i])

for i in range(n):
    soma = soma + (v1[i]*v2[i])

print(f"O produto escalar vale {soma:.2f}.")