def formatar_pilha(pilha: list[int]) -> list[int]:
    """Retorna a pilha com o topo primeiro, apenas para exibição."""
    # Na lista Python o topo fica no FINAL; invertemos só para exibir
    return list(reversed(pilha))


def dfs_pilha(lista: list[list[int]], inicio: int) -> list[int]:
    """Executa a DFS iterativa com pilha explícita e retorna a ordem de visitação."""
    # PASSO 1 – PREPARAÇÃO
    # Inicialmente nenhum vértice foi visitado
    visitado = [False] * len(lista)

    # Guarda a sequência em que os vértices são visitados
    ordem = []

    # PASSO 2 – CRIAÇÃO DA PILHA
    # A lista funciona como pilha (LIFO): o topo é o último elemento
    pilha = []

    # O vértice inicial é o primeiro a entrar na pilha
    pilha.append(inicio)
    print(f"Pilha inicial (topo primeiro): {formatar_pilha(pilha)}")

    # PASSO 3 – EXECUÇÃO DA DFS
    iteracao = 0
    while pilha:
        iteracao += 1

        # Retira o elemento que está no topo da pilha
        u = pilha.pop()
        print(f"\nIteração {iteracao}: retirou {u} do topo")

        # Um mesmo vértice pode ter sido empilhado por caminhos diferentes.
        # Por isso, verificamos novamente se ele já foi visitado.
        if visitado[u]:
            print(f"  {u} já foi visitado, ignorado")
            print(f"  Pilha (topo primeiro): {formatar_pilha(pilha)}")
            print(f"  Visitados: {ordem}")
            continue

        # Marca o vértice como visitado e registra na sequência
        visitado[u] = True
        ordem.append(u)
        print(f"  Vizinhos de {u}: {lista[u]}")

        # Para visitar os menores vértices primeiro, empilhamos os
        # vizinhos em ordem decrescente, pois a pilha é LIFO
        empilhados = []
        for v in reversed(lista[u]):
            if not visitado[v]:
                # O vizinho é colocado no topo da pilha
                pilha.append(v)
                empilhados.append(v)

        print(f"  Empilhados: {empilhados}")
        print(f"  Pilha (topo primeiro): {formatar_pilha(pilha)}")
        print(f"  Visitados: {ordem}")

    return ordem