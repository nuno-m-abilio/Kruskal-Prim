import heapq
from typing import Dict, List, Optional, Set, Tuple
from leitura_dados import aresta


def prim_lista(adjacencias: Dict[int, List[aresta]], vertices_ids: List[int], r: Optional[int] = None
)-> Tuple[List[aresta], float]:
    '''Algoritmo de Prim usando busca linear para encontrar o próximo vértice (O(V²)). O argumento
    r é o vértice que o algoritmo vai iniciar por. Retorna a tupla (MST, custo_total) onde MST é
    lista de arestas da árvore geradora mínima.'''

    if not vertices_ids:
        return [], 0.0
        
    if r is None:
        r = vertices_ids[0]
    
    # Dicionários de Prim
    # peso[v]: Menor peso de uma aresta que conecta v a algum vértice já na MST
    # pred[v]: Predecessor de v na MST. O tipo é Optional[int]
    peso: Dict[int, float] = {v: float('inf') for v in vertices_ids}
    pred: Dict[int, Optional[int]] = {v: None for v in vertices_ids}
    
    # Q: Conjunto de vértices que *ainda não* estão na MST
    Q: Set[int] = set(vertices_ids)
    
    peso[r] = 0
    mst: List[aresta] = []
    custo_total: float = 0.0
    
    # 6. Enquanto Q não for vazio
    while Q:
        # 7. u <- Extrai-Min(Q) - Busca Linear
        min_peso = float('inf')
        u: Optional[int] = None # Anotação para 'u' que pode ser None
        
        for v in Q:
            if peso[v] < min_peso:
                min_peso = peso[v]
                u = v
        
        # Se não encontramos um u, significa que o grafo não é conexo (ou Q está vazio)
        if u is None:
            break
            
        Q.remove(u)
        
        predecessor = pred[u] # Usamos uma variável local para checagem de tipo
        
        # Se u não for a raiz e tiver um predecessor, adiciona a aresta na MST
        # Checar 'is not None' garante ao Mypy que 'predecessor' é 'int'
        if predecessor is not None:
            # Encontrar a aresta real (u, pred[u]) na lista de adjacência (ou recriar)
            aresta_mst = None
            for a in adjacencias[u]:
                # Como pred[u] é int aqui, não há erro de tipo
                if a.id_v2 == predecessor: 
                    aresta_mst = a
                    break
            
            if aresta_mst:
                # Armazenamos a aresta (u, pred[u]) - ou (pred[u], u)
                # Como predecessor é int, não há erro ao passá-lo para id_v2
                mst.append(aresta(id_v1=u, id_v2=predecessor, peso=peso[u]))
                custo_total += peso[u]
            
        # 8. Para cada vértice v adjacente a u
        for aresta_u_v in adjacencias.get(u, []):
            v = aresta_u_v.id_v2
            w_u_v = aresta_u_v.peso
            
            # 9. Se v está em Q e w(u,v) < peso(v)
            if v in Q and w_u_v < peso[v]:
                # 10. pred(v) <- u; 11. peso(v) <- w(u,v);
                pred[v] = u # u é int, compatível com Optional[int]
                peso[v] = w_u_v # Atualiza o peso de corte
                
    return mst, custo_total

def prim_heap(adjacencias: Dict[int, List[aresta]], vertices_ids: List[int], r: Optional[int] = None
) -> Tuple[List[aresta], float]:
    """
    Algoritmo de Prim usando Min-Heap (Fila de Prioridade) para encontrar o próximo vértice (O(E log V)).
    
    Args:
        adjacencias: Dicionário de adjacências {id_v: [aresta, ...]}.
        vertices_ids: Lista com IDs de todos os vértices.
        r: ID do vértice inicial. Se None, usa o primeiro da lista.
    
    Returns:
        Tupla (MST, custo_total) onde MST é lista de arestas da árvore geradora mínima.
    """
    
    if not vertices_ids:
        return [], 0.0
        
    if r is None:
        r = vertices_ids[0]
        
    # Inicialização dos dicionários de Prim
    peso: Dict[int, float] = {v: float('inf') for v in vertices_ids}
    pred: Dict[int, Optional[int]] = {v: None for v in vertices_ids}
    
    # Min-Heap (Q): armazena (peso, id_vertice)
    # Anotação de tipo para o heap, que é uma lista de tuplas (float, int)
    Q: List[Tuple[float, int]] = []
    
    peso[r] = 0
    # Adiciona todos os vértices ao Min-Heap, mas o peso de r é 0
    for v in vertices_ids:
        heapq.heappush(Q, (peso[v], v))
        
    mst: List[aresta] = []
    custo_total: float = 0.0
    
    # Conjunto para rastrear quais vértices *já foram* incluídos na MST
    na_mst: Set[int] = set()
    
    # 6. Enquanto Q não for vazio
    while Q and len(na_mst) < len(vertices_ids):
        # 7. u <- Extrai-Min(Q)
        w_u, u = heapq.heappop(Q)
        
        if u in na_mst:
            continue # Já processado com um peso menor ou igual
            
        na_mst.add(u)
        
        predecessor = pred[u]
        
        # Adiciona a aresta à MST
        # Checar 'is not None' garante ao Mypy que 'predecessor' é 'int'
        if predecessor is not None:
            # Armazena a aresta (u, pred[u])
            mst.append(aresta(id_v1=u, id_v2=predecessor, peso=peso[u]))
            custo_total += peso[u]
            
        # 8. Para cada vértice v adjacente a u
        for aresta_u_v in adjacencias.get(u, []):
            v = aresta_u_v.id_v2
            w_u_v = aresta_u_v.peso
            
            # 9. Se v ainda não está na MST e w(u,v) < peso(v)
            if v not in na_mst and w_u_v < peso[v]:
                # 10. pred(v) <- u; 11. peso(v) <- w(u,v);
                pred[v] = u
                peso[v] = w_u_v
                # Insere o novo peso no heap.
                heapq.heappush(Q, (peso[v], v))
                
    return mst, custo_total