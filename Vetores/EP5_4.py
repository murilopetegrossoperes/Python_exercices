#Nesta atividade, você deve implementar três funções complementares para gerenciar um vetor de 10 elementos inteiros:
#inserir: Lê os dados e retorna o vetor preenchido.
#imprimir: Exibe os elementos separados por espaço.
#shift: Desloca cada elemento uma posição para a direita de forma circular (o último torna-se o primeiro).

def inserir():
    v = [0] * 10
    for i in range(len(v)):
        # Insere dado na posição específica
        v[i] = int(input())
    # código para ler 10 valores
    return v

def imprimir(v):
    # código para imprimir com espaços e quebra de linha ao final
     # Insere dado na posição específica
  print(*v)


def shift(v):
    n = len(v)
    if n > 1: # Só faz sentido deslocar se tiver mais de 1 elemento
        # 1. Guardamos o último elemento
        ultimo_elemento = v[n - 1] 
        
        # 2. Deslocamos os elementos para a direita usando o for
        # Começamos no último índice e vamos voltando (-1) até o índice 1
        for i in range(n - 1, 0, -1):
            v[i] = v[i - 1] 
            
        # 3. Colocamos o último elemento na primeira posição
        v[0] = ultimo_elemento