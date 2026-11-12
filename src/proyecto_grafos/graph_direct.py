class Direct_Graph:
    #Grafo dirigido representado mediante una matriz de adyacencia.

    #matrix[i][j] almacena el peso del arco que va del vértice i al vértice j, o None si dicho arco no existe (por lo que un peso de 0 sigue siendo válido).
    

    def __init__(self):
        self.vertices = []   # etiquetas de los vértices, en el orden de inserción
        self.index = {}      # etiqueta -> posición de fila/columna en la matriz
        self.matrix = []     # Matriz de pesos de tamaño |V| x |V|

    def add_vertex(self, vertex):
        if vertex in self.index:
            return
        self.index[vertex] = len(self.vertices)
        self.vertices.append(vertex)
        for row in self.matrix:
            row.append(None)
        self.matrix.append([None] * len(self.vertices))

    def add_edge(self, source, target, weight=1):
        self.add_vertex(source)
        self.add_vertex(target)
        self.matrix[self.index[source]][self.index[target]] = weight

    def remove_edge(self, source, target):
        if self.has_edge(source, target):
            self.matrix[self.index[source]][self.index[target]] = None

    def has_edge(self, source, target):
        if source not in self.index or target not in self.index:
            return False
        return self.matrix[self.index[source]][self.index[target]] is not None

    def get_weight(self, source, target):
        if not self.has_edge(source, target):
            return None
        return self.matrix[self.index[source]][self.index[target]]

    def out_neighbors(self, vertex):
        row = self.matrix[self.index[vertex]]
        return [self.vertices[j] for j, w in enumerate(row) if w is not None]

    def in_neighbors(self, vertex):
        j = self.index[vertex]
        return [self.vertices[i] for i, row in enumerate(self.matrix) if row[j] is not None]

    def out_degree(self, vertex):
        return len(self.out_neighbors(vertex))

    def in_degree(self, vertex):
        return len(self.in_neighbors(vertex))

    def edges(self):
        #Devuelve todos los arcos como tuplas (origen, destino, peso).
        result = []
        for i, row in enumerate(self.matrix):
            for j, w in enumerate(row):
                if w is not None:
                    result.append((self.vertices[i], self.vertices[j], w))
        return result

    def __str__(self):
        lines = ["    " + " ".join(f"{v:>3}" for v in self.vertices)]
        for v, row in zip(self.vertices, self.matrix):
            cells = " ".join(f"{'-' if w is None else w:>3}" for w in row)
            lines.append(f"{v:>3} {cells}")
        return "\n".join(lines)
