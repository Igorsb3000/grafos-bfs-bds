# Algoritmos de Grafos em Python

Programa com menu que implementa os algoritmos estudados na disciplina de **Teoria dos Grafos (UFRN)**: representações de grafos, buscas em largura e profundidade, verificação de árvore, árvores geradoras e arborescência, além da visualização gráfica do grafo.

## Requisitos

- Python 3.10 ou superior (desenvolvido com **Python 3.14**)
- Bibliotecas listadas em `requirements.txt`:
  - `networkx` e `matplotlib`, para desenhar o grafo

## Instalação das dependências

**Terminal**, dentro da pasta do projeto:

```bash
pip install -r requirements.txt
```

**PyCharm:** abra o arquivo `requirements.txt` e clique em **Install requirements** no aviso que aparece no topo do editor.

## Estrutura

```
projeto/
├── main.py                       # Menu e ponto de entrada do programa
├── requirements.txt
├── README.md
├── utils/
│   ├── entrada.py                # Leitura e validação de dados do usuário
│   ├── matriz_adjacencia.py      # Matriz de adjacência
│   └── lista_adjacencia.py       # Lista de adjacência (direcionada e não direcionada)
├── buscas/
│   ├── bfs.py                    # Busca em largura (fila)
│   ├── dfs_recursiva.py          # Busca em profundidade recursiva
│   └── dfs_pilha.py              # Busca em profundidade com pilha
└── arvores/
    ├── arvore_geradora_bfs.py    # Árvore geradora por BFS
    ├── arvore_geradora_dfs.py    # Árvore geradora por DFS
    └── arborescencia_bfs.py      # Arborescência em grafo direcionado
```

## Como executar

**PyCharm:** abra a pasta do projeto, clique com o botão direito em `main.py` e escolha **Run 'main'**. Nas próximas vezes, basta clicar no botão ▶ no canto superior direito.

**Terminal**, dentro da pasta do projeto:

```bash
python main.py
```

No Windows, o comando também pode ser `py main.py`; no macOS e Linux, `python3 main.py`.

## Uso

Ao iniciar, o programa pede os dados do grafo:

1. Quantidade de vértices (numerados de `0` a `n - 1`)
2. Quantidade de arestas
3. Cada aresta, informando os dois vértices
4. Vértice inicial

O grafo deve ser **simples**: não são aceitos laços nem arestas repetidas. Em seguida, o menu é exibido:

| Opção | Funcionalidade |
|---|---|
| 1 | Exibe a matriz de adjacência |
| 2 | Exibe a lista de adjacência |
| 3 | Executa a busca em largura (BFS) |
| 4 | Executa a busca em profundidade recursiva |
| 5 | Executa a busca em profundidade com pilha |
| 6 | Mostra os conjuntos V e E e desenha o grafo em uma janela |
| 7 | Verifica se o grafo é uma árvore (conexo e com V − 1 arestas) |
| 8 | Constrói a árvore geradora por BFS |
| 9 | Constrói a árvore geradora por DFS |
| 10 | Constrói a arborescência por BFS |
| 11 | Compara as árvores geradoras obtidas por BFS e DFS |
| 0 | Encerra o programa |

Observações:

- Nas opções de busca e de árvore geradora, o programa pede o vértice inicial.
- Na opção 6, o menu volta a aparecer depois que a janela do gráfico é fechada.
- Na opção 10, cada aresta `(u, v)` é interpretada como um arco `u → v`, na ordem em que foi digitada. Se algum vértice não for alcançável a partir da raiz escolhida, o programa informa falha.
