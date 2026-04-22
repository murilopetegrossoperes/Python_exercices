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

## 📝 Lista de Exercícios

### Parte 1: Vetores (1D)
1. **Soma Manual:** Crie um programa que percorra um vetor de números e calcule a soma total.
2. **O Maior do Rebanho:** Encontre o maior e o menor valor de um vetor sem usar `max()` ou `min()`.
3. **Busca Linear:** Verifique se um número `X` existe no vetor e retorne sua posição. Se não existir, retorne `-1`.
4. **Inversão de Valores:** Inverta a ordem dos elementos de um vetor (o primeiro vira o último, etc) sem criar um vetor novo e sem usar `[::-1]`.
5. **Média e Desvio:** Calcule a média aritmética e conte quantos elementos estão acima da média.

### Parte 2: Matrizes (2D)
1. **Varredura Total:** Dada uma matriz 3x3, calcule a soma de todos os seus elementos.
2. **Identidade Visual:** Verifique se uma matriz quadrada é uma Matriz Identidade (1 na diagonal principal e 0 no restante).
3. **Diagonal Principal:** Extraia apenas os elementos da diagonal principal de uma matriz e coloque-os em um vetor.
4. **Matriz Transposta:** Crie uma nova matriz que seja a transposta da original (linhas viram colunas).
5. **Busca em Coordenadas:** Peça um valor ao usuário e diga em qual linha e coluna ele se encontra na matriz.

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

Para te ajudar a visualizar essa movimentação de índices e como a lógica de busca funciona sem funções prontas, preparei o simulador abaixo:

```json?chameleon
{"component":"LlmGeneratedComponent","props":{"height":"600px","prompt":"Crie um simulador interativo de 'Busca Linear na Marra' em um vetor. O usuário deve poder inserir uma lista de números (vetor) e um número alvo para buscar. O simulador deve mostrar visualmente um ponteiro (índice 'i') percorrendo cada posição do vetor passo a passo. Para cada passo, deve mostrar a comparação lógica: 'O valor no índice i é igual ao alvo?'. Se encontrar, destaca o sucesso; se chegar ao fim sem encontrar, mostra que o valor não existe. Inclua controles de 'Próximo Passo' e 'Reiniciar'. Tudo em português.","id":"im_c25a38a0302b0642"}}
