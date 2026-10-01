def ler_inteiro(mensagem: str) -> int:
    """Repete a leitura até o usuário digitar um número inteiro válido."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def ler_vertice(n: int, mensagem: str = "Vértice inicial: ") -> int:
    """Lê um vértice válido entre 0 e n - 1."""
    vertice = ler_inteiro(mensagem)
    # Repete a leitura enquanto o vértice não existir no grafo
    while not (0 <= vertice < n):
        vertice = ler_inteiro(f"Informe um vértice entre 0 e {n - 1}: ")
    return vertice


def ler_grafo() -> tuple[int, list[tuple[int, int]]]:
    """Lê do usuário a quantidade de vértices e as arestas de um grafo simples."""
    # Leitura da quantidade de vértices (n)
    n = ler_inteiro("Insira a quantidade de vértices: ")
    while n <= 0:
        n = ler_inteiro("O grafo precisa ter ao menos 1 vértice: ")

    # Um grafo simples com n vértices tem no máximo n(n-1)/2 arestas
    max_arestas = n * (n - 1) // 2
    m = ler_inteiro("Insira a quantidade de arestas: ")
    while not (0 <= m <= max_arestas):
        m = ler_inteiro(f"Informe entre 0 e {max_arestas} arestas: ")

    # Leitura das arestas: só adiciona quando a aresta for válida
    arestas = []
    while len(arestas) < m:
        print(f"Insira a aresta {len(arestas) + 1} de {m}:")
        u = ler_inteiro("Primeiro vértice: ")
        v = ler_inteiro("Segundo vértice: ")

        # Os dois vértices precisam existir no grafo
        if not (0 <= u < n and 0 <= v < n):
            print(f"Vértices devem estar entre 0 e {n - 1}.")
        # Grafo simples: não permite laço
        elif u == v:
            print("Laços não são permitidos em grafo simples.")
        # Grafo simples: não permite aresta repetida, em nenhum dos sentidos
        elif (u, v) in arestas or (v, u) in arestas:
            print(f"A aresta ({u},{v}) já foi inserida.")
        else:
            arestas.append((u, v))

    return n, arestas