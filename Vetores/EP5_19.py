#você deve processar o desempenho de uma turma. O objetivo é calcular a média aritmética das notas de n alunos e, em seguida, identificar e listar apenas os nomes daqueles que superaram essa média.
n = int(input())
itens_linha1 = input().split(" ")
itens_linha2 = input().split(" ")
soma = 0 
alunos=[0]*n
notas=[0]*n

for i in range(n):
    alunos[i] = (itens_linha1[i])
for i in range(n):
    notas[i] = int(itens_linha2[i])
for i in range(n):
    soma = soma + notas[i]
média = soma/n

for i in range(n):
    if notas[i] > média:
        print(alunos[i])
