def arvore_geradora_dfs(lista: list[list[int]], inicio: int) -> list[tuple[int, int]]:
    # VISITADOS: inicialmente nenhum vértice foi visitado
    visitado = [False] * len(lista)

    # PILHA (LIFO): guarda pares (vértice, pai), o topo é o final da lista
    pilha = []

    # T: guarda somente as arestas que pertencem à árvore geradora
    arvore = []

    # A raiz entra na pilha sem pai (None equivale ao NULO do pseudocódigo)
    pilha.append((inicio, None))

    while pilha:
        # Retira do topo o próximo vértice e de quem ele foi alcançado
        u, pai = pilha.pop()

        # Um vértice pode ter sido empilhado mais de uma vez;
        # só é processado na primeira vez em que sai da pilha
        if not visitado[u]:
            visitado[u] = True

            # ARESTA DA ÁRVORE: se u não é a raiz, (pai, u) é a aresta de descoberta
            if pai is not None:
                arvore.append((pai, u))
                print(f"Aresta ({pai},{u}) adicionada à árvore")

            # Empilha os vizinhos em ordem inversa, para o menor sair primeiro;
            # cada um é empilhado junto com u, que será seu pai se for visitado
            for v in reversed(lista[u]):
                if not visitado[v]:
                    pilha.append((v, u))

    return arvore