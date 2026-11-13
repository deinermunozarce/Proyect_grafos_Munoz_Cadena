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


class GrafoNoDirigido:
    def __init__(self):
        self.Vertexs = {}     # nombre -> objeto Vertice
        self.Edges = []      # lista de objetos arista

    def add_vertex(self, name ):
        # Si el vértice no existe todavía, lo creamos
        if name not in self.Vertexs:
            self.Vertexs[name] = Vertex(name)
        return self.Vertexs[name]

    def add_edge(self, name_a, name_b, weight=1):
        a = self.add_vertex(name_a)
        b = self.add_vertex(name_b)

        self.Edges.append(Edge(a, b, weight))

        # No dirigido: a<-->b
        a.partners.append(b)
        b.partners.append(a)

    def show(self):
        for name, Vertex in self.Vertexs.items():
            nombres_partners = [v.name for v in Vertex.partners]
            print(f"{name} -> {nombres_partners}")
            
            
#------------------------PUNTO 6-------------------------------------------------------------
    def related(self):
            if len(self.Vertexs) == 0:        # grafo vacío
                return True
    
            # 1. Escoger un vértice cualquiera (el primero)
            start = list(self.Vertexs.values())[0]
    
            # 2. Recorrer desde ahí
            visited = []
            pila = [start]
    
            while len(pila) > 0:
                actual = pila.pop()
                if actual not in visited:
                    visited.append(actual)
                    for vecino in actual.partners:
                        pila.append(vecino)
    
            # 3. cuenta y conprueba si estan todos
            return len(visited) == len(self.Vertexs)    


#-------------------------PUNTO 4----------------------------------------------------

class GrafoDirigido:
    def __init__(self):
        self.Vertexs = {}     # nombre -> objeto Vertice
        self.Edges = []      # lista de objetos arista

    def add_vertex(self, name):
        if name not in self.Vertexs:
            self.Vertexs[name] = Vertex(name)
        return self.Vertexs[name]

    def add_edge(self, source, target, weight=1):
        a = self.add_vertex(source)
        b = self.add_vertex(target)

        self.Edges.append(Edge(a, b, weight))

        # Dirigido (source -> target)
        a.partners.append(b)

    def show(self):
        for name, Vertex in self.Vertexs.items():
            nombres_partners = [v.name for v in Vertex.partners]
            print(f"{name} -> {nombres_partners}")
            
#--------------------PUNTO 5------------------------------------------------------------

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
