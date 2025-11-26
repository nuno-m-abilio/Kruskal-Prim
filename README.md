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
- [x] Ler arquivos CSV de vértices (coordenadas)
- [x] Ler arquivos CSV de arestas
- [x] Calcular peso de uma aresta usando distância euclidiana
- [x] Criar tipo de dados Vértice
- [x] Criar tipo de dados Aresta
- [x] Transformar arquivo de entrada em uma lista de adjacência para o Prim
- [x] Inicializar listas de vértices e de arestas em formato de conjuntos para o Kruskal

### 2. Implementação do Algoritmo de Kruskal
- [x] Estrutura Union-Find com união por altura
- [x] Ordenação de arestas por peso
- [x] Algoritmo principal de Kruskal

### 3. Implementação do Algoritmo de Prim
- [x] Estrutura de heap/fila de prioridade
- [x] Algoritmo principal de Prim

### 4. Validação e Testes
- [x] Verificar corretude dos algoritmos
- [x] Validar custos das MSTs

### 5. Experimentos e Medições
- [x] Medir tempo de execução
- [x] Medir uso de memória
- [ ] Executar em múltiplas instâncias

### 6. Análise dos Resultados
- [ ] Gerar gráficos comparativos
- [ ] Interpretar resultados
- [ ] Escrever relatório final

## Como Executar

### 1. Instalação de Dependências

Para medir o uso de memória (funções Prim e Kruskal) é necessário instalar a biblioteca `psutil` e seu pacote de tipagem para Mypy:

```bash
pip install psutil
python -m pip install types-psutil
```

### 2. Execução

```bash
python main.py nodes.csv edges.csv kruskal_simples
python main.py nodes.csv edges.csv kruskal_rank
python main.py nodes.csv edges.csv kruskal_otimizado
python main.py nodes.csv edges.csv prim_lista
python main.py nodes.csv edges.csv prim_heap
python main.py nodes.csv edges.csv todos
```

## Estrutura do Projeto

```
├── main.py              # Arquivo principal
├── prim.py              # Implementação de Prim
├── kruskal.py           # Implementação de Kruskal
├── leitura_dados.py     # Leitura e processamento de CSVs
└── README.md            # Este arquivo
```