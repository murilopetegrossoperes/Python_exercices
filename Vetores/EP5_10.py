# o seu programa deve atuar como um filtro de duplicatas. O objetivo é ler um vetor de n inteiros e imprimir apenas a primeira ocorrência de cada número, eliminando as repetições subsequentes e mantendo a ordem original.
n = int(input())
itens_linha = input().split(" ")
i= 0
v=[0]*n

for i in range(n):
    v[i] = int(itens_linha[i])

for i in range(n):
    ja_apareceu = False
    for k in range(i): 
        if v[i] == v[k]:
            ja_apareceu = True
            break

    if not ja_apareceu:
          for j in range(n):
            if v[i] == v[j]:
                print(v[i], end=" ")
                break 