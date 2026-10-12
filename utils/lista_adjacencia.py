def criar_lista_nao_direcionada(n: int, arestas: list[tuple[int, int]]) -> list[list[int]]:
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

def criar_lista_direcionada(n: int, arcos: list[tuple[int, int]]) -> list[list[int]]:
    lista = [[] for _ in range(n)]

    # Cada arco (u, v) vai somente de u para v:
    # v entra na lista de u, mas u NÃO entra na lista de v
    for u, v in arcos:
        lista[u].append(v)

    # Mantém os vizinhos em ordem crescente
    for vizinhos in lista:
        vizinhos.sort()

    return lista

def exibir_lista(lista: list[list[int]]) -> None:
    # PASSO 3 – Exibição da lista
    for i in range(len(lista)):
        print(f"{i} → [", end="")
        # Percorre apenas os vizinhos existentes do vértice i
        for j, vizinho in enumerate(lista[i]):
            separador = ", " if j > 0 else ""
            print(f"{separador}{vizinho}", end="")
        print("]")
