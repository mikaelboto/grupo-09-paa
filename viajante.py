import itertools
import math

def calcular_distancia(ponto1, ponto2):
    """Calcula a distância euclidiana entre dois pontos."""
    return math.sqrt((ponto1[0] - ponto2[0])**2 + (ponto1[1] - ponto2[1])**2)

def resolver_caixeiro_viajante(pontos):
    """
    Possivel resolução do problema do Caixeiro Viajante (TSP) usando força bruta.
    
    Args:
        pontos (dict): Dicionário de pontos com o nome da cidade como chave e
                       suas coordenadas (x, y) como valor.
                       
    Returns:
        tuple: Uma tupla contendo a menor distância e a melhor rota.
    """
    bairros = list(pontos.keys())
    # O ponto de partida é fixo para simplificar o cálculo
    bairro_inicial = bairros[0]
    outros_bairros = bairros[1:]
    
    menor_distancia = float('inf')
    melhor_rota = None

    # Gera todas as permutações de rotas possíveis
    for rota_permutacao in itertools.permutations(outros_bairros):
        rota_atual = [bairro_inicial] + list(rota_permutacao) + [bairro_inicial]
        distancia_atual = 0
        
        # Calcula a distância total da rota atual
        for i in range(len(rota_atual) - 1):
            ponto_a = pontos[rota_atual[i]]
            ponto_b = pontos[rota_atual[i+1]]
            distancia_atual += calcular_distancia(ponto_a, ponto_b)
        
        # Atualiza a melhor rota e a menor distância
        if distancia_atual < menor_distancia:
            menor_distancia = distancia_atual
            melhor_rota = rota_atual
            
    return menor_distancia, melhor_rota

if __name__ == "__main__":
    bairros_exemplo = {
        'América': (0, 0),
        'Siqueira': (1, 5),
        'Luzia': (4, 3),
        'Jardins': (6, 2)
    }

    # Resolve o problema e exibe a possivel solução
    distancia_minima, rota_otima = resolver_caixeiro_viajante(bairros_exemplo)

    print(f"Bairros e coordenadas: {bairros_exemplo}")
    print(f"Melhor rota: {rota_otima}")
    print(f"Distância mínima: {distancia_minima:.2f}")
