from collections import deque

def arvore_geradora_bfs(lista: list[list[int]], inicio: int) -> list[tuple[int, int]]:
    # VISITADOS: inicialmente nenhum vértice foi visitado
    visitado = [False] * len(lista)

    # FILA (FIFO): vértices descobertos que ainda serão explorados
    fila = deque()

    # T: guarda somente as arestas que pertencem à árvore geradora
    arvore = []

    # A raiz é marcada e colocada na fila
    visitado[inicio] = True
    fila.append(inicio)

    while fila:
        # Retira o próximo vértice a ser explorado
        u = fila.popleft()

        # Percorre todos os vizinhos de u
        for v in lista[u]:
            # Só um vértice ainda não descoberto gera uma aresta da árvore
            if not visitado[v]:
                visitado[v] = True

                # ARESTA DA ÁRVORE: (u, v) foi usada para descobrir v
                arvore.append((u, v))
                print(f"Aresta ({u},{v}) adicionada à árvore")

                # v entra na fila para ter seus vizinhos explorados depois
                fila.append(v)

    return arvore


def exibir_arvore(n: int, arvore: list[tuple[int, int]], inicio: int) -> None:
    # Vértices presentes na árvore: a raiz e as duas pontas de cada aresta
    vertices = {inicio}
    for u, v in arvore:
        vertices.update((u, v))

    print("\nArestas da árvore:", ", ".join(f"({u},{v})" for u, v in arvore))
    print("Quantidade de vértices:", len(vertices))
    print("Quantidade de arestas:", len(arvore))

    # Validação: todos os vértices presentes e exatamente V - 1 arestas
    if len(vertices) == n and len(arvore) == n - 1:
        print(f"Válida: contém os {n} vértices e {n - 1} arestas (V - 1).")
    else:
        print("Inválida: o grafo não é conexo a partir da raiz escolhida.")