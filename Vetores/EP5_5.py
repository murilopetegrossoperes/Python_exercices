# você deve verificar se um elemento específico de um vetor atua como o "fiel da balança". O objetivo é descobrir se o valor armazenado em um índice escolhido é exatamente igual à soma de todos os outros elementos da sequência.

n = int(input())
soma = 0
v = [0] * n  

for i in range(n):
  v[i] = int(input()) 


for i in range(n):
  soma = soma + v[i] 

vetor_escolhido = int(input())
valor_final = soma - v[vetor_escolhido]

if valor_final == v[vetor_escolhido]:
  print("Sim")
else:
  print("Nao")