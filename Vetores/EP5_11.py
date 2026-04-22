#você deve desenvolver um programa para comparar dois conjuntos de dados. O objetivo é verificar se o vetor2 contém exatamente os mesmos elementos do vetor1, independentemente da ordem em que aparecem.

n1 = int(input())
v1 = [0] * n1
itens_linha1 = input().split(" ")
for i in range(n1):
    v1[i] = int(itens_linha1[i])

n2 = int(input())
v2 = [0] * n2
itens_linha2 = input().split(" ")
for i in range(n2):
    v2[i] = int(itens_linha2[i])

sao_iguais = 1 

if n1 != n2:
    sao_iguais = 0
else:

    for i in range(n1):
        numero_alvo = v1[i] 
        
        conta_v1 = 0
        conta_v2 = 0
        
        for j in range(n1):
            if v1[j] == numero_alvo:
                conta_v1 += 1
                
        for j in range(n2):
            if v2[j] == numero_alvo:
                conta_v2 += 1
                  
        if conta_v1 != conta_v2:
            sao_iguais = 0 
            break 

if sao_iguais == 1:
    for i in range(n1):
     print(v1[i], end=" ")
    print()
    for i in range(n2):
        print(v2[i], end=" ")
    print()

    print("OK")
else:
    for i in range(n1):
     print(v1[i], end=" ")
    print()

    for i in range(n2):
     print(v2[i], end=" ")
    print()

    print("Erro")