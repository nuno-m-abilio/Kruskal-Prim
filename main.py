import sys
import leitura_dados as le
import kruskal as kr
import prim as pr
import time

def main():
    if len(sys.argv) != 4:
        print("Uso: python main.py <nodes.csv> <edges.csv> <algoritmo>")
        print("\nAlgoritmos disponíveis:")
        print("  - kruskal_simples")
        print("  - kruskal_rank")
        print("  - kruskal_otimizado")
        print("  - prim_lista")
        print("  - prim_heap")
        print("  - todos")
        sys.exit(1)
    
    arquivo_vertices = sys.argv[1]
    arquivo_arestas = sys.argv[2]
    algoritmo = sys.argv[3].lower()
    
    algoritmos_validos = ['kruskal_simples', 'kruskal_rank', 'kruskal_otimizado', 
                          'prim_lista', 'prim_heap']
    
    if algoritmo not in algoritmos_validos:
        print(f"Erro: algoritmo '{algoritmo}' inválido")
        print("Algoritmos válidos:", ", ".join(algoritmos_validos))
        sys.exit(1)
    
    print(f"Lendo vértices de: {arquivo_vertices}")
    print(f"Lendo arestas de: {arquivo_arestas}")
    print(f"Executando: {algoritmo}\n")
    
    tempo_inicio = time.perf_counter() # Marcando o início do tempo
    memoria_inicio = le.medir_uso_memoria_processo() # Marcando pico de memória inicial

    vertices = le.dict_vertices(arquivo_vertices)
    vertices_ids = list(vertices.keys())
    print(f"Total de vértices: {len(vertices)}")
  
    if algoritmo in ['kruskal_simples']:
        print("\nExecutando Kruskal Simples (Union-Find sem otimizações)")
        arestas = le.lista_arestas(arquivo_arestas, vertices)
        print(f"Total de arestas: {len(arestas)}")
        
        mst, custo = kr.kruskal_simples(arestas, vertices_ids)
        print(f"MST encontrada com {len(mst)} arestas")
        print(f"Custo total: {custo:.2f}")
        tempo_fim = time.perf_counter()
        memoria_fim = le.medir_uso_memoria_processo()

    elif algoritmo in ['kruskal_rank']:
        print("\nExecutando Kruskal com Union by Rank")
        arestas = le.lista_arestas(arquivo_arestas, vertices)
        print(f"Total de arestas: {len(arestas)}")
        
        mst, custo = kr.kruskal_rank(arestas, vertices_ids)
        print(f"MST encontrada com {len(mst)} arestas")
        print(f"Custo total: {custo:.2f}")
        tempo_fim = time.perf_counter()
        memoria_fim = le.medir_uso_memoria_processo()
    
    elif algoritmo in ['kruskal_otimizado']:
        print("\nExecutando Kruskal Otimizado (Rank + Path Compression)")
        arestas = le.lista_arestas(arquivo_arestas, vertices)
        print(f"Total de arestas: {len(arestas)}")
        
        mst, custo = kr.kruskal_otimizado(arestas, vertices_ids)
        print(f"MST encontrada com {len(mst)} arestas")
        print(f"Custo total: {custo:.2f}")
        tempo_fim = time.perf_counter()
        memoria_fim = le.medir_uso_memoria_processo()

    elif algoritmo in ['prim_lista']:
        print("\nExecutando Prim com Busca Linear (O(n²))")
        adjacencias = le.struct_adjacencia(arquivo_arestas, vertices) 
        vertice_raiz = vertices_ids[0]

        mst, custo = pr.prim_lista(adjacencias, vertices_ids, r=vertice_raiz)
        print(f"MST encontrada com {len(mst)} arestas")
        print(f"Custo total: {custo:.2f}")
        tempo_fim = time.perf_counter()
        memoria_fim = le.medir_uso_memoria_processo()

    elif algoritmo in ['prim_heap']:
        print("\nExecutando Prim com Heap Binário (O(m log n))")
        adjacencias = le.struct_adjacencia(arquivo_arestas, vertices)
        vertice_raiz = vertices_ids[0]
       
        mst, custo = pr.prim_heap(adjacencias, vertices_ids, r=vertice_raiz)
        print(f"MST encontrada com {len(mst)} arestas")
        print(f"Custo total: {custo:.2f}")
        tempo_fim = time.perf_counter()
        memoria_fim = le.medir_uso_memoria_processo()

    tempo_total = tempo_fim - tempo_inicio
    memoria_consumida = memoria_fim - memoria_inicio
    print(f"Tempo de execução: {tempo_total:.4f} segundos")
    print(f"Uso de memória (aumento): {memoria_consumida:.2f} MB")

if __name__ == "__main__":  
    main()