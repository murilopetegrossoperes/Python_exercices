#você deve calcular o desvio padrão amostral (σ) de um conjunto de n números reais. O desvio padrão indica o quanto os dados variam em relação à média aritmética (μ).

n = int(input())
cordenada_x1_y1_z1 = input().split(" ")
soma = 0
somatoria = 0 
v1 = [0] * n

for i in range(n):
    v1[i] = float(cordenada_x1_y1_z1[i])

for i in range(n):
    soma = soma + (v1[i])

média = soma/n
for i in range(n):
    somatoria = somatoria + ((v1[i] - média)**2)

somatoria_final = somatoria/(n-1)
d = somatoria_final**0.5

print(f"O desvio padrao vale {d:.2f}.")