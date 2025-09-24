import itertools
import math
import matplotlib.pyplot as plt
import networkx as nx

def calcular_distancia(ponto1, ponto2):
    """Calcula a distância euclidiana entre dois pontos."""
    return math.sqrt((ponto1[0] - ponto2[0])**2 + (ponto1[1] - ponto2[1])**2)

def resolver_caixeiro_viajante(pontos):
    """
    Possível resolução do problema do Caixeiro Viajante (TSP) usando força bruta.

    Args:
        pontos (dict): Dicionário de pontos com o nome da cidade como chave e
                       suas coordenadas (x, y) como valor.

    Returns:
        tuple: Uma tupla contendo a menor distância, a melhor rota e todas as rotas com suas distâncias.
    """
    bairros = list(pontos.keys())
    bairro_inicial = bairros[0]
    outros_bairros = bairros[1:]

    menor_distancia = float('inf')
    melhor_rota = None
    rotas_distancias = []

    # Gera todas as permutações de rotas possíveis
    for rota_permutacao in itertools.permutations(outros_bairros):
        rota_atual = [bairro_inicial] + list(rota_permutacao) + [bairro_inicial]
        distancia_atual = 0

        # Calcula a distância total da rota atual
        for i in range(len(rota_atual) - 1):
            ponto_a = pontos[rota_atual[i]]
            ponto_b = pontos[rota_atual[i+1]]
            distancia_atual += calcular_distancia(ponto_a, ponto_b)

        rotas_distancias.append((distancia_atual, rota_atual))

        if distancia_atual < menor_distancia:
            menor_distancia = distancia_atual
            melhor_rota = rota_atual

    return menor_distancia, melhor_rota, rotas_distancias

def desenhar_todas_rotas(pontos, rotas_distancias, rota_otima):
    """Desenha todas as rotas em subplots lado a lado."""
    n = len(rotas_distancias)
    cols = 3  # número de colunas por linha
    rows = math.ceil(n / cols)

    fig, axes = plt.subplots(rows, cols, figsize=(cols*5, rows*4))
    axes = axes.flatten()

    for i, (dist, rota) in enumerate(rotas_distancias):
        G = nx.Graph()
        for bairro, coords in pontos.items():
            G.add_node(bairro, pos=coords)

        edges = [(rota[j], rota[j+1]) for j in range(len(rota)-1)]
        G.add_edges_from(edges)
        pos = nx.get_node_attributes(G, 'pos')

        ax = axes[i]
        nx.draw(G, pos, with_labels=True, node_size=800, node_color="lightgray",
                font_weight="bold", font_size=10, ax=ax)

        nx.draw_networkx_edges(
            G, pos, edgelist=edges, width=2,
            edge_color="red" if rota == rota_otima else "gray",
            ax=ax
        )

        ax.set_title(f"Rota {i+1}: {rota}\nDistância: {dist:.2f}")

    # Remove eixos extras caso sobre espaço
    for j in range(i+1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    bairros_exemplo = {
        'América': (0, 0),
        'Siqueira': (1, 5),
        'Luzia': (4, 3),
        'Jardins': (6, 2)
    }

    distancia_minima, rota_otima, rotas_distancias = resolver_caixeiro_viajante(bairros_exemplo)

    print(f"Bairros: {bairros_exemplo}")
    print(f"Melhor rota: {rota_otima}")
    print(f"Distância mínima: {distancia_minima:.2f}")

    # Desenha todas as rotas em um único gráfico
    desenhar_todas_rotas(bairros_exemplo, rotas_distancias, rota_otima)
