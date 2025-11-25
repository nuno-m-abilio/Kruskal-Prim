import sys
import leitura_dados as le

def main():
    # Verificar argumentos
    if len(sys.argv) != 4:
        print("Uso: python main.py <nodes.csv> <edges.csv> <prim|kruskal|ambos>")
        sys.exit(1)
    
    arquivo_vertices = sys.argv[1]
    arquivo_arestas = sys.argv[2]
    algoritmo = sys.argv[3].lower()
    
    # Validar algoritmo
    if algoritmo not in ['prim', 'kruskal', 'ambos']:
        print("Erro: algoritmo deve ser 'prim', 'kruskal' ou 'ambos'")
        sys.exit(1)
    
    print(f"Lendo vértices de: {arquivo_vertices}")
    print(f"Lendo arestas de: {arquivo_arestas}")
    print(f"Executando: {algoritmo}\n")
    
    # Carregar vértices (sempre necessário)
    vertices = le.dict_vertices(arquivo_vertices)
    print(f"Total de vértices: {len(vertices)}")
    
    # Executar Kruskal
    if algoritmo in ['kruskal', 'ambos']:
        print("\n=== Executando Kruskal ===")
        arestas = le.lista_arestas(arquivo_arestas, vertices)
    
    # Executar Prim
    if algoritmo in ['prim', 'ambos']:
        print("\n=== Executando Prim ===")
        adjacencias = le.struct_adjacencia(arquivo_arestas, vertices)
        print(adjacencias)


if __name__ == "__main__":
    main()