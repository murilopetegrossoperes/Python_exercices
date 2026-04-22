#Ache o maior elemento do vetor

n = int(input())
i= 1
v=[0]*n

max = (int(input()))
v[0] = max

while i<n:
  v[i] = int(input())
  i+=1
for j in (v):
    if j > max: 
      max = j
print(max)