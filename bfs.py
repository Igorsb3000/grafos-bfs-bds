from collections import deque


def bfs(lista: list[list[int]], inicio: int) -> list[int]:
    """Executa a busca em largura a partir de inicio e retorna a ordem de visitação."""
    # Inicialmente nenhum vértice foi visitado
    visitado = [False] * len(lista)

    # Fila (FIFO) que armazena os vértices descobertos que ainda serão processados
    fila = deque()

    # Guarda a ordem em que os vértices são visitados
    ordem = []

    # O vértice inicial é marcado e colocado na fila
    visitado[inicio] = True
    fila.append(inicio)
    print(f"Fila inicial: {list(fila)}")

    # A busca continua enquanto houver elementos na fila
    iteracao = 0
    while fila:
        iteracao += 1

        # Retira o primeiro elemento da fila (o que entrou primeiro)
        u = fila.popleft()
        ordem.append(u)
        print(f"\nIteração {iteracao}: retirou {u} da fila")
        print(f"  Vizinhos encontrados: {lista[u]}")

        # Guarda apenas os vizinhos que entrarem na fila nesta iteração
        adicionados = []

        # Analisa todos os vizinhos de u
        for v in lista[u]:
            # Só processa um vizinho que ainda não foi visitado
            if not visitado[v]:
                # Marca antes de enfileirar para evitar duplicações na fila
                visitado[v] = True
                # O vizinho entra no fim da fila e será processado depois
                fila.append(v)
                adicionados.append(v)

        # Vértices marcados como visitados até o momento
        visitados = [v for v in range(len(lista)) if visitado[v]]

        print(f"  Novos adicionados: {adicionados}")
        print(f"  Fila: {list(fila)}")
        print(f"  Visitados: {visitados}")

    return ordem