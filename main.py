from entrada import ler_inteiro, ler_vertice, ler_grafo
from matriz_adjacencia import criar_matriz, exibir_matriz
from lista_adjacencia import criar_lista, exibir_lista
from bfs import bfs
from dfs_recursiva import dfs_recursiva
from dfs_pilha import dfs_pilha
from rich import print
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
0 - Sair
================================="""


def mostrar_grafo(n: int, arestas: list[tuple[int, int]]) -> None:
    """Exibe os conjuntos de vértices e arestas do grafo."""
    print("V = {" + ", ".join(str(v) for v in range(n)) + "}")
    print("E = {" + ", ".join(f"({u},{v})" for u, v in arestas) + "}")

    """Cria e exibe a representação visual do grafo em uma janela separada."""
    G = nx.Graph()
    G.add_nodes_from(range(n))
    G.add_edges_from(arestas)

    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color="skyblue",
            node_size=800, font_size=14, font_weight="bold")
    plt.show()



def exibir_sequencia(ordem: list[int]) -> None:
    """Exibe a sequência de visitação de uma busca."""
    print("\nSequência de visitação:", " → ".join(str(v) for v in ordem))


def main() -> None:
    # O grafo é mantido como n + arestas; as representações derivam dele
    n, arestas = ler_grafo()
    lista = criar_lista(n, arestas)

    while True:
        print(MENU)
        opcao = ler_inteiro("Escolha uma opção: ")

        match opcao:
            case 1:
                exibir_matriz(criar_matriz(n, arestas))
            case 2:
                exibir_lista(lista)
            case 3:
                exibir_sequencia(bfs(lista, ler_vertice(n)))
            case 4:
                exibir_sequencia(dfs_recursiva(lista, ler_vertice(n)))
            case 5:
                exibir_sequencia(dfs_pilha(lista, ler_vertice(n)))
            case 6:
                mostrar_grafo(n, arestas)
            case 0:
                print("Encerrando...")
                break
            case _:
                print("Opção inválida.")


if __name__ == '__main__':
    main()