from proyecto_grafos.graph_direct import Direct_Graph
from proyecto_grafos.graph_reader import load_graph_from_file
#---------------------PUNTO 3----------------------------------------
class Vertex:
    def __init__(self, name):
        self.name = name
        self.partners = []      # lista de objetos Vertice

class Edge:
   
    def __init__(self, source, target, weight=1):
        self.source = source   # objeto Vertice
        self.target = target # objeto Vertice
        self.weight = weight

class Undirected_graph:

    def __init__(self):
        self.vertexs = {}     # nombre -> objeto Vertex
        self.edges = []       # lista de objetos Edge

    def add_vertex(self, name):
        # Si el vértice no existe todavía, lo creamos
        if name not in self.vertexs:
            self.vertexs[name] = Vertex(name)
        return self.vertexs[name]

    def add_edge(self, name_a, name_b, weight=1):
        a = self.add_vertex(name_a)
        b = self.add_vertex(name_b)
        self.edges.append(Edge(a, b, weight))
        # No dirigido: a<-->b
        a.partners.append(b)
        b.partners.append(a)

    def show(self):
        # CORRECCIÓN: la variable "Vertex" tapaba la clase Vertex; ahora es "vertex"
        for name, vertex in self.vertexs.items():
            partner_names = [v.name for v in vertex.partners]
            print(f"{name} -> {partner_names}")

    # ------------------------ Funciones auxiliares (NO imprimen) ------------------------

    def count_components(self):
        """Cuenta las componentes conexas (pedazos) del grafo."""
        visited = set()   # CORRECCIÓN: set en vez de lista (búsqueda más rápida)
        components = 0

        for start in self.vertexs.values():
            if start not in visited:
                components = components + 1      # encontramos un pedazo nuevo

                # Recorrido en profundidad (DFS) con pila
                stack = [start]
                while len(stack) > 0:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        for partner in current.partners:
                            stack.append(partner)

        return components

    def _connected(self):
        # Un grafo es conexo si tiene a lo sumo 1 componente (el vacío cuenta como conexo)
        return self.count_components() <= 1

    def _has_cycles(self):
        V = len(self.vertexs)           # cantidad de vértices
        E = len(self.edges)             # cantidad de aristas
        C = self.count_components()     # cantidad de componentes
        # Sin ciclos solo puede haber V - C aristas; si hay más, hay un ciclo
        return E > V - C

    # ------------------------ PUNTO 6 ------------------------

    def is_connected(self):
        result = self._connected()
        print(f"es_conexo: {result}")
        return result

    # ------------------------ PUNTO 7 ------------------------

    def has_cycles(self):
        result = self._has_cycles()
        print(f"tiene_ciclos: {result}")
        return result

    # ------------------------ PUNTO 8 ------------------------

    def is_tree(self):
        result = len(self.vertexs) > 0 and self._connected() and not self._has_cycles()
        print(f"es_arbol: {result}")
        return result

    # ------------------------ PUNTO 9 ------------------------

    def is_forest(self):
        result = not self._has_cycles()
        print(f"es_bosque: {result}")
        return result