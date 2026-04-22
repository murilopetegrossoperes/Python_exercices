#você deve processar um vetor de 5 números reais para extrair três informações: a contagem de números negativos, a soma dos números positivos e a verificação de existência de um valor específico.
n = 5
existe = 0
neg = 0
i = 0 
soma=0
v = [0]*n

itens_linha = input().split(" ")
num_escolhido = int(input())

while i<n:
    v[i] = int(itens_linha[i])
    i+=1

i = 0 
while i < n:
    if v[i] == num_escolhido:
      existe += 1
      i += 1
    else:
      i += 1

i=0
while i < n:
    if v[i] < 0:
      neg += 1
      i += 1
    else:
      soma = soma + v[i]
      i += 1


print(neg)
print(soma)
if existe == 1:
  print("Existe!")
else:
  print("Nao existe!")

