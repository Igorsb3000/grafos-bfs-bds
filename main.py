from utils.entrada import ler_inteiro, ler_vertice, ler_grafo
from utils.matriz_adjacencia import criar_matriz, exibir_matriz
from buscas.bfs import bfs
from buscas.dfs_recursiva import dfs_recursiva
from buscas.dfs_pilha import dfs_pilha
from arvores.arvore_geradora_bfs import arvore_geradora_bfs, exibir_arvore
from arvores.arvore_geradora_dfs import arvore_geradora_dfs
from utils.lista_adjacencia import criar_lista_nao_direcionada, criar_lista_direcionada, exibir_lista
from arvores.arborescencia_bfs import arborescencia_bfs
import networkx as nx
import matplotlib.pyplot as plt

MENU = """
=================================
ALGORITMOS DE GRAFOS
=================================
1 - Criar Matriz de Adjacência
2 - Criar Lista de Adjacência
3 - Executar BFS
4 - Executar DFS Recursiva
5 - Executar DFS com Pilha
6 - Mostrar Grafo
7 - Verificar se Grafo é Árvore
8 - Criar Árvore Geradora BFS
9 - Criar Árvore Geradora DFS
10 - Arborescencia BFS
11 - Comparar resultado de BFS e DFS para Árvore Geradora
0 - Sair
================================="""


def eh_arvore(numero_vertices: int, arestas: list[tuple[int, int]],
              lista: list[list[int]], inicio: int) -> bool:
    print("Quantidade de arestas =", len(arestas))
    print("Quantidade de vértices =", numero_vertices)
    print("Início do grafo =", inicio)

    # 1. Uma árvore com V vértices tem exatamente V - 1 arestas.
    #    Se a contagem for diferente, o grafo é descartado sem percorrê-lo.
    #
    #    A contagem sozinha não é suficiente: um grafo pode ter V - 1 arestas
    #    e ainda assim ter um ciclo em um componente e vértices isolados em outro.
    #    Por isso também é preciso testar a conectividade.
    if len(arestas) != numero_vertices - 1:
        return False

    # 2 e 3. A BFS a partir de inicio registra os vértices alcançáveis
    ordem, visitados = bfs(lista, inicio)
    print("VISITADOS =", visitados)

    # 4. Se todos foram alcançados, o grafo é conexo; com V - 1 arestas, é árvore
    return len(visitados) == numero_vertices

def comparar_arvores(arvore_bfs: list[tuple[int, int]],
                     arvore_dfs: list[tuple[int, int]]) -> None:
    # Normaliza cada aresta como (menor, maior), pois (5,4) e (4,5) são a mesma aresta
    bfs = {tuple(sorted(a)) for a in arvore_bfs}
    dfs = {tuple(sorted(a)) for a in arvore_dfs}

    print("Árvore BFS:  ", sorted(bfs))
    print("Árvore DFS:  ", sorted(dfs))
    print("Em comum:    ", sorted(bfs & dfs))
    print("Só na BFS:   ", sorted(bfs - dfs))
    print("Só na DFS:   ", sorted(dfs - bfs))

def mostrar_se_eh_grafo(ehGrafo: bool) -> None:
    if ehGrafo: print("### Grafo É uma árvore. ###")
    else: print("### Grafo NÃO É uma árvore. ###")

def mostrar_grafo(n: int, arestas: list[tuple[int, int]], inicio: int) -> None:
    print("V = {" + ", ".join(str(v) for v in range(n)) + "}")
    print("E = {" + ", ".join(f"({u},{v})" for u, v in arestas) + "}")

    G = nx.Graph()
    G.add_nodes_from(range(n))
    G.add_edges_from(arestas)

    pos = calcular_posicoes(G, inicio)
    nx.draw(G, pos, with_labels=True, node_color="skyblue",
            node_size=800, font_size=14, font_weight="bold")
    plt.show()


def exibir_sequencia(ordem: list[int], visitados: list[int] | None = None) -> None:
    print("\nSequência de visitação:", " → ".join(str(v) for v in ordem))
    if visitados is not None:
        print("Visitados:", ", ".join(str(v) for v in visitados))

def calcular_posicoes(G: nx.Graph, inicio: int) -> dict[int, tuple[float, float]]:
    # Distância (nível) de cada vértice alcançável a partir do início
    distancias = nx.single_source_shortest_path_length(G, inicio)

    # Vértices não alcançáveis (grafo desconexo) vão para uma camada extra no final
    ultimo_nivel = max(distancias.values()) + 1
    for v in G.nodes:
        distancias.setdefault(v, ultimo_nivel)

    # Agrupa os vértices por nível, em ordem crescente
    niveis: dict[int, list[int]] = {}
    for v, nivel in sorted(distancias.items()):
        niveis.setdefault(nivel, []).append(v)

    # Cada nível é uma linha (y negativo, para descer); os vértices são centralizados em x
    posicoes = {}
    for nivel, vertices in niveis.items():
        for i, v in enumerate(vertices):
            x = i - (len(vertices) - 1) / 2
            posicoes[v] = (x, -nivel)
    return posicoes

def main() -> None:
    # O grafo é mantido como n + arestas; as representações derivam dele
    n, arestas = ler_grafo()
    lista = criar_lista_nao_direcionada(n, arestas)
    # inicio = ler_inteiro("Insira o valor inicio do vértice: ")
    inicio = ler_vertice(n, "Insira o vértice inicial: ")

    while True:
        print(MENU)
        opcao = ler_inteiro("Escolha uma opção: ")

        match opcao:
            case 1:
                exibir_matriz(criar_matriz(n, arestas))
            case 2:
                exibir_lista(lista)
            case 3:
                ordem, visitados = bfs(lista, ler_vertice(n))
                exibir_sequencia(ordem)
            case 4:
                exibir_sequencia(dfs_recursiva(lista, ler_vertice(n)))
            case 5:
                exibir_sequencia(dfs_pilha(lista, ler_vertice(n)))
            case 6:
                mostrar_grafo(n, arestas, inicio)
            case 7:
                mostrar_se_eh_grafo(eh_arvore(n, arestas, lista, inicio))
            case 8:
                inicio = ler_vertice(n)
                arvore = arvore_geradora_bfs(lista, inicio)
                exibir_arvore(n, arvore, inicio)
            case 9:
                inicio = ler_vertice(n)
                arvore = arvore_geradora_dfs(lista, inicio)
                exibir_arvore(n, arvore, inicio)
            case 10:
                # Reaproveita as arestas já informadas, agora lidas como arcos u → v
                lista_dir = criar_lista_direcionada(n, arestas)
                raiz = ler_vertice(n, "Raiz da arborescência: ")
                arborescencia = arborescencia_bfs(lista_dir, raiz)
                if arborescencia is not None:
                    print("Arcos da arborescência:",
                          ", ".join(f"{u}→{v}" for u, v in arborescencia))
            case 11:
                inicio = ler_vertice(n)
                comparar_arvores(arvore_geradora_bfs(lista, inicio),
                                 arvore_geradora_dfs(lista, inicio))
            case 0:
                print("Encerrando...")
                break
            case _:
                print("Opção inválida.")


if __name__ == '__main__':
    main()