#o desafio é identificar elementos comuns entre dois conjuntos. Você deve ler dois vetores, x e y, de 5 elementos cada, e criar um terceiro vetor I contendo apenas os números que aparecem em ambos, sem repetições no resultado final.
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
indice_v3 = 0

for i in range(n):
    ja_apareceu = False
    
    for k in range(i): 
        if v1[i] == v1[k]:
            ja_apareceu = True
            break

    if not ja_apareceu:
        for j in range(n):
            if v1[i] == v2[j]:
                v3[indice_v3] = v1[i]
                
                indice_v3 += 1
                
                break 

print("O vetor intersecção é ", end="")
v4 = [0]*indice_v3
for i in range(indice_v3):
    v4[i] = v3[i]
print(v4)
