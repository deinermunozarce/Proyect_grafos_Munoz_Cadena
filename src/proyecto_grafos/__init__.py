from proyecto_grafos.graph_direct import Direct_Graph
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
        self.vertexs = {}     # nombre -> objeto Vertice
        self.edges = []      # lista de objetos arista

    def add_vertex(self, name ):
        # Si el vértice no existe todavía, lo creamos
        if name not in self.vertexs:
            self.vertexs[name] = Vertex(name)
        return self.vertexs[name]

    def add_edge(self, name_a, name_b, weight=1):
        a = self.add_vertex(name_a)
        b = self.add_vertex(name_b)

        self.Edges.append(Edge(a, b, weight))

        # No dirigido: a<-->b
        a.partners.append(b)
        b.partners.append(a)

    def show(self):
        for name, Vertex in self.vertexs.items():
            nombres_partners = [v.name for v in Vertex.partners]
            print(f"{name} -> {nombres_partners}")
            
            
#------------------------PUNTO 6-------------------------------------------------------------
    def related(self):
            if len(self.vertexs) == 0:        # grafo vacío
                return True
    
            #  Escoger un vértice cualquiera (el primero)
            start = list(self.vertexs.values())[0]
    
            #  Recorrer desde ahí
            visited = []
            pila = [start]
    
            while len(pila) > 0:
                actual = pila.pop()
                if actual not in visited:
                    visited.append(actual)
                    for partner in actual.partners:
                        pila.append(partner)
    
            #  cuenta y conprueba si estan todos
            return len(visited) == len(self.vertexs) 
        
#-------------------------PUNTO 7--------------------------------------------------------   
    def count_components(self):
            visited = []
            components = 0
    
            for start in self.vertexs.values():
                if start not in visited:
                    components = components + 1      # encontramos un pedazo nuevo
    
                    # Recorrido normal (igual que en es_conexo)
                    pila = [start]
                    while len(pila) > 0:
                        actual = pila.pop()
                        if actual not in visited:
                            visited.append(actual)
                            for partner in actual.partners:
                                pila.append(partner)
    
            return components
        
    def tiene_ciclos(self):
            V = len(self.vertexs)           # cantidad de vértices
            E = len(self.edges)            # cantidad de aristas
            C = self.count_components()    # cantidad de pedazos
                         
            # Sin ciclos solo puede haber V - C aristas
            return E > V - C      
            
        
#--------------------PUNTO 5------------------------------------------------------------

"""
def load_grafo(ruta, grafo):
    archivo = open(ruta, "r")
    text = archivo.read()          # lee todo como texto
    archivo.close()

    lines = text.split("\n")      # separa el texto en líneas

    for i in range(len(lines)):
        line = lines[i]


        # Separar la línea por comas y va recorriendo carácter por carácter
        parts = []
        actual = ""
        for caracter in line:
            if caracter == ",":
                parts.append(actual)
                actual = ""
            else:
                actual = actual + caracter
        parts.append(actual)       # agrega el último pedazo

        source = parts[0]
        target = parts[1]
        weight = int(parts[2])

        grafo.add_edge(source, target, weight)
"""