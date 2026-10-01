# Algoritmos de Grafos em Python

Programa com menu que implementa os algoritmos da lista de exercícios de **Teoria dos Grafos (UFRN)**: matriz de adjacência, lista de adjacência, BFS, DFS recursiva e DFS com pilha, além da visualização gráfica do grafo.

## Requisitos

- Python 3.10 ou superior (desenvolvido com **Python 3.14**)
- Bibliotecas `networkx` e `matplotlib`, usadas para desenhar o grafo

## Instalação das dependências

**Terminal**, dentro da pasta do projeto:

```bash
pip install -r requirements.txt
```

**PyCharm:** abra o arquivo `requirements.txt` e clique em **Install requirements** no aviso que aparece no topo do editor.

## Estrutura

| Arquivo | Conteúdo |
|---|---|
| `main.py` | Menu e ponto de entrada do programa |
| `entrada.py` | Leitura e validação de dados do usuário |
| `grafo_exemplo.py` | Grafo utilizado na atividade |
| `matriz_adjacencia.py` | Matriz de adjacência |
| `lista_adjacencia.py` | Lista de adjacência |
| `bfs.py` | Busca em largura (fila) |
| `dfs_recursiva.py` | Busca em profundidade recursiva |
| `dfs_pilha.py` | Busca em profundidade com pilha |
| `requirements.txt` | Bibliotecas necessárias |

Todos os arquivos devem ficar na mesma pasta.

## Como executar

**PyCharm:** abra a pasta do projeto, clique com o botão direito em `main.py` e escolha **Run 'main'**. Nas próximas vezes, basta clicar no botão ▶ no canto superior direito.

**Terminal**, dentro da pasta do projeto:

```bash
python main.py
```

No Windows, o comando também pode ser `py main.py`; no macOS e Linux, `python3 main.py`.

Ao executar, escolha uma opção do menu. Nas buscas (opções 3, 4 e 5), o programa pede o vértice inicial.