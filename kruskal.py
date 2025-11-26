from leitura_dados import aresta

class UnionFindSimples:
    '''Union-Find sem otimizações'''
    def __init__(self, vertices_ids: list[int]):
        self.pai = {v: v for v in vertices_ids}
    
    def find(self, x: int) -> int:
        '''Encontra a raiz do conjunto que contém x'''
        if self.pai[x] != x:
            return self.find(self.pai[x])  # Sem path compression
        return self.pai[x]
    
    def union(self, x: int, y: int) -> bool:
        '''Une os conjuntos que contêm x e y. Retorna True se uniu, False se já estavam unidos'''
        raiz_x = self.find(x)
        raiz_y = self.find(y)
        
        if raiz_x == raiz_y:
            return False
        
        # Sem otimização - sempre anexa y em x
        self.pai[raiz_y] = raiz_x
        return True


class UnionFindRank:
    '''Union-Find com união por rank (altura)'''
    def __init__(self, vertices_ids: list[int]):
        self.pai = {v: v for v in vertices_ids}
        self.rank = {v: 0 for v in vertices_ids}
    
    def find(self, x: int) -> int:
        '''Encontra a raiz do conjunto que contém x'''
        if self.pai[x] != x:
            return self.find(self.pai[x])  # Sem path compression
        return self.pai[x]
    
    def union(self, x: int, y: int) -> bool:
        '''Une os conjuntos que contêm x e y usando union by rank'''
        raiz_x = self.find(x)
        raiz_y = self.find(y)
        
        if raiz_x == raiz_y:
            return False
        
        # União por rank: anexa árvore menor na maior
        if self.rank[raiz_x] < self.rank[raiz_y]:
            self.pai[raiz_x] = raiz_y
        elif self.rank[raiz_x] > self.rank[raiz_y]:
            self.pai[raiz_y] = raiz_x
        else:
            self.pai[raiz_y] = raiz_x
            self.rank[raiz_x] += 1
        
        return True


class UnionFindOtimizado:
    '''Union-Find com união por rank e path compression'''
    def __init__(self, vertices_ids: list[int]):
        self.pai = {v: v for v in vertices_ids}
        self.rank = {v: 0 for v in vertices_ids}
    
    def find(self, x: int) -> int:
        '''Encontra a raiz do conjunto que contém x com path compression'''
        if self.pai[x] != x:
            self.pai[x] = self.find(self.pai[x])  # Path compression
        return self.pai[x]
    
    def union(self, x: int, y: int) -> bool:
        '''Une os conjuntos que contêm x e y usando union by rank'''
        raiz_x = self.find(x)
        raiz_y = self.find(y)
        
        if raiz_x == raiz_y:
            return False
        
        # União por rank: anexa árvore menor na maior
        if self.rank[raiz_x] < self.rank[raiz_y]:
            self.pai[raiz_x] = raiz_y
        elif self.rank[raiz_x] > self.rank[raiz_y]:
            self.pai[raiz_y] = raiz_x
        else:
            self.pai[raiz_y] = raiz_x
            self.rank[raiz_x] += 1
        
        return True


def kruskal_simples(arestas: list[aresta], vertices_ids: list[int]) -> tuple[list[aresta], float]:
    '''Algoritmo de Kruskal usando Union-Find simples (sem otimizações). Retorna a tupla
   (MST,custo_total) onde MST é lista de arestas da árvore geradora mínima'''
    mst = []
    custo_total = 0.0
    uf = UnionFindSimples(vertices_ids)
    arestas.sort(key=lambda a: a.peso)
    
    for a in arestas:
        if uf.union(a.id_v1, a.id_v2):
            mst.append(a)
            custo_total += a.peso

            if len(mst) == len(vertices_ids) - 1:
                break
    
    return mst, custo_total


def kruskal_rank(arestas: list[aresta], vertices_ids: list[int]) -> tuple[list[aresta], float]:
    '''Algoritmo de Kruskal usando Union-Find com união por rank. Retorna a tupla
    (MST, custo_total) onde MST é lista de arestas da árvore geradora mínima'''
    mst = []
    custo_total = 0.0
    uf = UnionFindRank(vertices_ids)
    arestas.sort(key=lambda a: a.peso)
    
    for a in arestas:
        if uf.union(a.id_v1, a.id_v2):
            mst.append(a)
            custo_total += a.peso
            
            if len(mst) == len(vertices_ids) - 1:
                break
    
    return mst, custo_total


def kruskal_otimizado(arestas: list[aresta], vertices_ids: list[int]) -> tuple[list[aresta], float]:
    '''Algoritmo de Kruskal usando Union-Find com união por rank e path compression. Retorna a
    tupla (MST, custo_total) onde MST é lista de arestas da árvore geradora mínima'''
    mst = []
    custo_total = 0.0
    uf = UnionFindOtimizado(vertices_ids)
    arestas.sort(key=lambda a: a.peso)
    
    for a in arestas:
        if uf.union(a.id_v1, a.id_v2):
            mst.append(a)
            custo_total += a.peso
            
            if len(mst) == len(vertices_ids) - 1:
                break
    
    return mst, custo_total