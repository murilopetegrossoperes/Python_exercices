#o objetivo é capturar cinco valores inteiros, armazená-los em um vetor e realizar dois procedimentos: exibir a sequência lida e calcular a média aritmética desses valores.
n = 5
v = [0] * n
soma = 0 
itens_linha = input().split(" ")
for i in range(n):
    v[i] = int(itens_linha[i])
    
for i in range(n):
  print(v[i], end=" ")
print()
for i in range(n):
    soma = soma + v[i]

media = soma/n
print(f"{media:.2f}")