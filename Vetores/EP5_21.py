#você deve implementar seu próprio algoritmo de ordenação. O objetivo é ler um vetor de n elementos e organizá-los em ordem crescente (do menor para o maior).

n = int(input())
v1 = [0] * n
itens_linha = input().split(" ")

for i in range(n):
    v1[i] = int(itens_linha[i])

for i in range(n):
    
    for j in range(n - 1):
        
        if v1[j] > v1[j + 1]:
            temp = v1[j]
            v1[j] = v1[j + 1]
            v1[j + 1] = temp


for i in range(n):
    print(v1[i], end=" ")