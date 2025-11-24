# Prim vs Kruskal - Árvore Geradora Mínima

Implementação e comparação dos algoritmos de **Prim** e **Kruskal** para cálculo de Árvore Geradora Mínima (MST) em grafos.

## Sobre o Projeto

Este trabalho avalia o desempenho dos algoritmos de Prim e Kruskal em diferentes instâncias de grafos. Os vértices possuem coordenadas UTM e o peso das arestas é calculado pela distância euclidiana entre eles.

## Objetivos

- Implementar Prim (com heap) e Kruskal (com Union-Find)
- Comparar tempo de execução e uso de memória
- Analisar como o desempenho varia com o tamanho dos grafos

## Checklist de Desenvolvimento

### 1. Leitura e Tratamento dos Dados
- [ ] Ler arquivos CSV de vértices (coordenadas)
- [ ] Ler arquivos CSV de arestas
- [ ] Calcular peso de uma aresta usando distância euclidiana
- [ ] Criar tipo de dados Vértice
- [ ] Criar tipo de dados Aresta
- [ ] Transformar arquivo de entrada em uma lista de adjacência para o Prim
- [ ] Inicializar listas de vértices e de arestas em formato de conjuntos para o Kruskal

### 2. Implementação do Algoritmo de Kruskal
- [ ] Estrutura Union-Find com união por altura
- [ ] Ordenação de arestas por peso
- [ ] Algoritmo principal de Kruskal

### 3. Implementação do Algoritmo de Prim
- [ ] Estrutura de heap/fila de prioridade
- [ ] Algoritmo principal de Prim

### 4. Validação e Testes
- [ ] Verificar corretude dos algoritmos
- [ ] Tratar grafos desconexos
- [ ] Validar custos das MSTs

### 5. Experimentos e Medições
- [ ] Medir tempo de execução
- [ ] Medir uso de memória
- [ ] Executar em múltiplas instâncias

### 6. Análise dos Resultados
- [ ] Gerar gráficos comparativos
- [ ] Interpretar resultados
- [ ] Escrever relatório final

## Como Executar

```bash
python main.py --vertices vertices.csv --arestas arestas.csv --algoritmo prim
```

## Estrutura do Projeto

```
├── main.py              # Arquivo principal
├── prim.py              # Implementação de Prim
├── kruskal.py           # Implementação de Kruskal
└── README.md            # Este arquivo
```