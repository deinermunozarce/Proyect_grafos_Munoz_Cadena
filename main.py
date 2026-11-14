from proyecto_grafos import Direct_Graph, load_graph_from_file
from proyecto_grafos import Undirected_graph


def check(descripcion, obtenido, esperado):
    estado = "OK " if obtenido == esperado else "FALLO"
    print(f"  [{estado}] {descripcion}: obtenido={obtenido!r}, esperado={esperado!r}")
    return obtenido == esperado


def prueba_punto_3():
    print("\n=== PUNTO 3: Grafo no dirigido (listas de adyacencia) ===")
    g = Undirected_graph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("D", "E", 5)
    g.show()
    ok = check("n.º de vértices", len(g.vertexs), 5)
    ok &= check("n.º de aristas", len(g.edges), 3)
    ok &= check("vecinos de B", [v.name for v in g.vertexs["B"].partners], ["A", "C"])
    return ok


def prueba_punto_4():
    print("\n=== PUNTO 4: Grafo dirigido (matriz de adyacencia) ===")
    g = Direct_Graph()
    g.add_edge("A", "B", 3)
    g.add_edge("B", "C", 0)      # peso 0 sigue siendo un arco válido
    g.add_edge("C", "A", 4)
    print(g)
    ok = check("A->B existe", g.has_edge("A", "B"), True)
    ok &= check("B->A existe (dirigido)", g.has_edge("B", "A"), False)
    ok &= check("peso B->C (0 válido)", g.get_weight("B", "C"), 0)
    ok &= check("vecinos salientes de A", g.out_neighbors("A"), ["B"])
    ok &= check("vecinos entrantes de A", g.in_neighbors("A"), ["C"])
    ok &= check("grado de salida de C", g.out_degree("C"), 1)
    g.remove_edge("A", "B")
    ok &= check("A->B tras remove_edge", g.has_edge("A", "B"), False)
    ok &= check("arcos restantes", g.edges(), [("B", "C", 0), ("C", "A", 4)])
    return ok


def prueba_punto_5():
    print("\n=== PUNTO 5: Lectura de grafo desde archivo ===")
    g = load_graph_from_file("datos_grafo.txt", Direct_Graph())
    print(g)
    ok = check("vértices", g.vertices, ["A", "B", "C", "D", "E"])
    ok &= check("peso A->B (entero)", g.get_weight("A", "B"), 3)
    ok &= check("peso B->C (decimal)", g.get_weight("B", "C"), 2.5)
    ok &= check("peso C->A (cero)", g.get_weight("C", "A"), 0)
    ok &= check("n.º de arcos", len(g.edges()), 5)
    return ok


def prueba_punto_6():
    print("\n=== PUNTO 6: Conexidad ===")
    vacio = Undirected_graph()
    ok = check("grafo vacío es conexo", vacio.related(), True)

    conexo = Undirected_graph()
    conexo.add_edge("A", "B")
    conexo.add_edge("B", "C")
    ok &= check("A-B-C es conexo", conexo.related(), True)

    no_conexo = Undirected_graph()
    no_conexo.add_edge("A", "B")
    no_conexo.add_edge("C", "D")
    ok &= check("A-B y C-D NO es conexo", no_conexo.related(), False)
    return ok


def prueba_punto_7():
    print("\n=== PUNTO 7: Componentes y ciclos ===")
    arbol = Undirected_graph()
    arbol.add_edge("A", "B")
    arbol.add_edge("B", "C")
    ok = check("componentes del árbol", arbol.count_components(), 1)
    ok &= check("árbol tiene ciclos", arbol.tiene_ciclos(), False)

    ciclo = Undirected_graph()
    ciclo.add_edge("A", "B")
    ciclo.add_edge("B", "C")
    ciclo.add_edge("C", "A")
    ok &= check("triángulo tiene ciclos", ciclo.tiene_ciclos(), True)

    dos = Undirected_graph()
    dos.add_edge("A", "B")
    dos.add_edge("C", "D")
    dos.add_vertex("E")
    ok &= check("componentes (A-B, C-D, E)", dos.count_components(), 3)
    ok &= check("bosque sin ciclos", dos.tiene_ciclos(), False)

    mixto = Undirected_graph()
    mixto.add_edge("A", "B")
    mixto.add_edge("B", "C")
    mixto.add_edge("C", "A")
    mixto.add_edge("X", "Y")
    ok &= check("componentes (triángulo + X-Y)", mixto.count_components(), 2)
    ok &= check("mixto tiene ciclos", mixto.tiene_ciclos(), True)
    return ok


def main():
    pruebas = [prueba_punto_3, prueba_punto_4, prueba_punto_5,
               prueba_punto_6, prueba_punto_7]
    resultados = [p() for p in pruebas]
    print("\n" + "=" * 50)
    if all(resultados):
        print("TODAS LAS PRUEBAS (puntos 3 a 7) PASARON")
    else:
        print("HAY PRUEBAS FALLIDAS:",
              [i + 3 for i, r in enumerate(resultados) if not r])


if __name__ == "__main__":
    main()