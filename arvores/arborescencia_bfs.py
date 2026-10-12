from collections import deque


def arborescencia_bfs(lista: list[list[int]], raiz: int) -> list[tuple[int, int]] | None:
    # VISITADOS: inicialmente nenhum vértice foi visitado
    visitado = [False] * len(lista)

    # FILA (FIFO) da busca em largura
    fila = deque()

    # A: arcos que pertencem à arborescência
    arborescencia = []

    # A raiz é o ponto de partida da estrutura
    visitado[raiz] = True
    fila.append(raiz)

    while fila:
        u = fila.popleft()

        # Como o grafo é direcionado, lista[u] contém apenas os arcos que SAEM de u
        for v in lista[u]:
            # Um arco só é usado se descobrir um vértice novo
            if not visitado[v]:
                visitado[v] = True

                # ARCO DA ARBORESCÊNCIA: (u, v) conecta o novo vértice à estrutura
                arborescencia.append((u, v))
                fila.append(v)

    # FALHA: algum vértice não pode ser alcançado a partir da raiz
    inalcancaveis = [v for v in range(len(lista)) if not visitado[v]]
    if inalcancaveis:
        print(f"FALHA: vértices inalcançáveis a partir de {raiz}: {inalcancaveis}")
        return None

    return arborescencia