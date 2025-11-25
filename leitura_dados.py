from dataclasses import dataclass
import csv

@dataclass
class vertice:
    id: int
    x: float
    y: float

@dataclass
class aresta:
    id_v1: int
    id_v2: int
    peso: float

def distancia(v1: vertice, v2: vertice) -> float:
    '''Distância entre dois vértices pela métrica Euclidiana'''
    return (((v1.x - v2.x)**2)+((v1.y - v2.y)**2))**(1/2)


def dict_vertices(arquivo_vertices: str) -> dict[int, vertice]:
    '''Lê o CSV de vértices e retorna um dicionário {id: vertice}. Formato esperado do CSV: id,x,y
    (com cabeçalho)'''
    vertices = {}
    with open(arquivo_vertices, 'r') as f:
        reader = csv.DictReader(f)
        for linha in reader:
            v = vertice(
                id=int(linha['id']),
                x=float(linha['x']),
                y=float(linha['y'])
            )
            vertices[v.id] = v
    return vertices


def lista_arestas(arquivo_arestas: str, vertices: dict[int, vertice]) -> list[aresta]:
    '''Lê o CSV de arestas e retorna uma lista de arestas com peso calculado. Usada para o
    algoritmo de Kruskal. Formato esperado do CSV: source,target (com cabeçalho)'''
    arestas = []
    with open(arquivo_arestas, 'r') as f:
        reader = csv.DictReader(f)
        for linha in reader:
            id_v1 = int(linha['source'])
            id_v2 = int(linha['target'])
            
            v1 = vertices[id_v1]
            v2 = vertices[id_v2]
            peso = distancia(v1, v2)
            
            a = aresta(id_v1=id_v1, id_v2=id_v2, peso=peso)
            arestas.append(a)
    
    return arestas


def struct_adjacencia(arquivo_arestas: str, vertices: dict[int, vertice]) -> dict[int, list[aresta]]:
    '''Cria uma lista de adjacências simples para uso com heap no algoritmo de Prim. Retorna um
    dicionário onde cada chave é um id de vértice e o valor é uma lista de arestas adjacentes.
    Formato esperado do CSV: source,target (com cabeçalho)'''
    adjacencias:dict[int, list[aresta]] = {id_v: [] for id_v in vertices.keys()}
    
    with open(arquivo_arestas, 'r') as f:
        reader = csv.DictReader(f)
        for linha in reader:
            id_v1 = int(linha['source'])
            id_v2 = int(linha['target'])
            
            v1 = vertices[id_v1]
            v2 = vertices[id_v2]
            peso = distancia(v1, v2)
            
            aresta_v1_v2 = aresta(id_v1=id_v1, id_v2=id_v2, peso=peso)
            aresta_v2_v1 = aresta(id_v1=id_v2, id_v2=id_v1, peso=peso)
            
            adjacencias[id_v1].append(aresta_v1_v2)
            adjacencias[id_v2].append(aresta_v2_v1)
    
    return adjacencias