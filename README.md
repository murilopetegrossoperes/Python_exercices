# Python_exercices

Este repositório contém uma série de desafios focados em manipulação de estruturas de dados lineares (vetores) e bidimensionais (matrizes) utilizando **lógica pura**.

## 🎯 Objetivo
O foco aqui é NÃO utilizar funções integradas (*built-in*) do Python sempre que possível. 
**Proibido usar:** `sum()`, `max()`, `min()`, `len()`, `list.sort()`, `list.reverse()`, `list.index()`, `list.count()`, ou bibliotecas como `numpy`.

## 🛠️ Regras de Ouro
1. Use apenas loops (`for`, `while`) e condicionais (`if`, `else`).
2. Para saber o tamanho de um vetor, tente passar o tamanho como parâmetro ou use um contador manual se necessário (embora `len()` seja aceitável em casos críticos, tente evitar).
3. Pense no índice: `vetor[i]` é seu melhor amigo.

---

## 🚀 Como executar
Basta ter o Python instalado (versão 3.x recomendada).
```bash
python nome_do_exercicio.py
```
---

### Entendendo a Lógica "Na Marra"

Para resolver esses exercícios, você precisa visualizar como o computador "enxerga" a matriz. Uma matriz nada mais é do que uma lista de listas. Para acessar um valor específico, você precisa de duas chaves: a **Linha (i)** e a **Coluna (j)**.



Quando você faz um exercício "na marra", você está simulando o comportamento de baixo nível da CPU: movendo um ponteiro de casa em casa. Por exemplo, para somar uma matriz, você faz um loop dentro de outro:
1. O primeiro loop fixa a **Linha 0**.
2. O segundo loop percorre todas as **Colunas** dessa linha.
3. Repete-se para a **Linha 1**, e assim por diante.
