def criar_matriz(n: int, arestas: list[tuple[int, int]]) -> list[list[int]]:
    # PASSO 1 – Criação e inicialização da matriz n x n com zeros
    # (inicialmente não há ligação entre nenhum par de vértices)
    matriz = [[0 for _ in range(n)] for _ in range(n)]

    # PASSO 2 – Inserção das arestas
    for u, v in arestas:
        # Registra a ligação u -> v e, por ser não direcionado, v -> u
        matriz[u][v] = 1
        matriz[v][u] = 1

    return matriz

def exibir_matriz(matriz: list[list[int]]) -> None:
    n = len(matriz)

    # PASSO 3 – Exibição da matriz
    # Rótulos das colunas
    print("     ", end="")
    for j in range(n):
        print(f"{j:>3}", end="")
    print()

    # Linhas da matriz, com o rótulo do vértice à esquerda
    for i in range(n):
        print(f" {i:>2} [", end="")
        for j in range(n):
            print(f"{matriz[i][j]:>3}", end="")
        print(" ]")