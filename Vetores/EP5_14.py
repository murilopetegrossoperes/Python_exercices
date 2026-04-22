#você deve processar um vetor de 10 posições para extrair informações específicas: listar os números pares e ímpares (sem repetições), além de identificar o maior e o menor valor da sequência.

n = 10
v = [0] * n
max = 0
min = 0

p = [0] * n
imp = [0] * n

indice_p = 0
indice_imp = 0

itens_linha = input().split(" ")
max = int(itens_linha[0])
min = int(itens_linha[0])

for i in range(n):
    v[i] = int(itens_linha[i])

    if v[i] > max:
        max = v[i]
    if v[i] < min:
        min = v[i]

    if v[i] % 2 == 0:
        p[indice_p] = v[i]

        indice_p += 1
    else:
        imp[indice_imp] = v[i]

        indice_imp += 1

print("Numeros pares:") 

for i in range(indice_p):
    ja_apareceu = False 
    for j in range(i):
        if p[i] == p[j]:
            ja_apareceu = True 
            break 
            
    if not ja_apareceu:

        print(p[i], end=" ")


if indice_p != 0:
    print()


print("Numeros impares:") 

for i in range(indice_imp):
    ja_apareceu = False
    for j in range(i):
        if imp[i] == imp[j]:
            ja_apareceu = True 
            break 
            
    if not ja_apareceu:
        print(imp[i], end=" ")

if indice_imp != 0:
    print()

print(f"Maior: {max}")
print(f"Menor: {min}")