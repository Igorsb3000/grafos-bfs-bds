def busca_profundidade(lista: list[list[int]], u: int, visitado: list[bool],
                       ordem: list[int], profundidade: int = 0) -> None:
    # Recuo proporcional à profundidade da chamada, para visualizar a recursão
    recuo = "  " * profundidade

    # Marca o vértice atual como visitado e registra na sequência
    visitado[u] = True
    ordem.append(u)
    print(f"{recuo}Entrando no vértice {u}")

    # Percorre todos os vizinhos de u
    for v in lista[u]:
        # Caso o vizinho ainda não tenha sido visitado,
        # a função chama a si própria para esse vértice (vai mais fundo)
        if not visitado[v]:
            busca_profundidade(lista, v, visitado, ordem, profundidade + 1)

    # Não há mais vizinhos não visitados: a chamada termina
    # e o controle volta para a chamada anterior (quem descobriu u)
    print(f"{recuo}Retornando do vértice {u}")


def dfs_recursiva(lista: list[list[int]], inicio: int) -> list[int]:
    # Inicialmente nenhum vértice foi visitado
    visitado = [False] * len(lista)

    # Guarda a sequência em que os vértices são visitados
    ordem = []

    # Inicia a busca pelo vértice escolhido
    busca_profundidade(lista, inicio, visitado, ordem)
    return ordem