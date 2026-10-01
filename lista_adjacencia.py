def criar_lista(n: int, arestas: list[tuple[int, int]]) -> list[list[int]]:
    """Cria a lista de adjacência de um grafo não direcionado."""
    # PASSO 1 – Criação das listas
    # Cada vértice começa com uma lista vazia (ainda sem vizinhos)
    lista = [[] for _ in range(n)]

    # PASSO 2 – Inserção das arestas
    for u, v in arestas:
        # O vértice v passa a ser vizinho de u
        lista[u].append(v)
        # Como o grafo é não direcionado, u também é vizinho de v
        lista[v].append(u)

    # Ordena os vizinhos de cada vértice em ordem crescente,
    # independentemente da ordem em que as arestas foram informadas
    for vizinhos in lista:
        vizinhos.sort()

    return lista


def exibir_lista(lista: list[list[int]]) -> None:
    """Exibe os vizinhos de cada vértice da lista de adjacência."""
    # PASSO 3 – Exibição da lista
    for i in range(len(lista)):
        print(f"{i} → [", end="")
        # Percorre apenas os vizinhos existentes do vértice i
        for j, vizinho in enumerate(lista[i]):
            separador = ", " if j > 0 else ""
            print(f"{separador}{vizinho}", end="")
        print("]")
