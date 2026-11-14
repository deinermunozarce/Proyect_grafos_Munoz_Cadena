import io
from contextlib import redirect_stdout

from proyecto_grafos import Direct_Graph, load_graph_from_file
from proyecto_grafos import Undirected_graph

failures = []   # aquí se guardan las pruebas fallidas (no se imprime nada si pasan)


def silent(function):
    """Ejecuta una función ocultando lo que imprime (para que las pruebas no ensucien la salida)."""
    with redirect_stdout(io.StringIO()):
        return function()


def check(description, obtained, expected):
    ok = obtained == expected
    if not ok:
        failures.append(f"{description}: obtenido={obtained!r}, esperado={expected!r}")
    return ok


def test_point_3():
    g = Undirected_graph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("D", "E", 5)
    check("P3 vértices", len(g.vertexs), 5)
    check("P3 aristas", len(g.edges), 3)
    check("P3 vecinos de B", [v.name for v in g.vertexs["B"].partners], ["A", "C"])


def test_point_4():
    g = Direct_Graph()
    g.add_edge("A", "B", 3)
    g.add_edge("B", "C", 0)      # peso 0 sigue siendo un arco válido
    g.add_edge("C", "A", 4)
    check("P4 A->B existe", g.has_edge("A", "B"), True)
    check("P4 B->A no existe", g.has_edge("B", "A"), False)
    check("P4 peso B->C", g.get_weight("B", "C"), 0)
    check("P4 salientes de A", g.out_neighbors("A"), ["B"])
    check("P4 entrantes de A", g.in_neighbors("A"), ["C"])
    g.remove_edge("A", "B")
    check("P4 tras remove_edge", g.has_edge("A", "B"), False)
    check("P4 arcos restantes", g.edges(), [("B", "C", 0), ("C", "A", 4)])


def test_point_5():
    g = load_graph_from_file("datos_grafo.txt", Direct_Graph())
    check("P5 vértices", g.vertices, ["A", "B", "C", "D", "E"])
    check("P5 peso entero", g.get_weight("A", "B"), 3)
    check("P5 peso decimal", g.get_weight("B", "C"), 2.5)
    check("P5 peso cero", g.get_weight("C", "A"), 0)
    check("P5 n.º de arcos", len(g.edges()), 5)


def test_point_6():
    empty = Undirected_graph()
    check("P6 vacío es conexo", silent(empty.is_connected), True)

    connected = Undirected_graph()
    connected.add_edge("A", "B")
    connected.add_edge("B", "C")
    check("P6 A-B-C conexo", silent(connected.is_connected), True)

    disconnected = Undirected_graph()
    disconnected.add_edge("A", "B")
    disconnected.add_edge("C", "D")
    check("P6 A-B y C-D no conexo", silent(disconnected.is_connected), False)


def test_point_7():
    path = Undirected_graph()
    path.add_edge("A", "B")
    path.add_edge("B", "C")
    check("P7 componentes del camino", path.count_components(), 1)
    check("P7 camino sin ciclos", silent(path.has_cycles), False)

    triangle = Undirected_graph()
    triangle.add_edge("A", "B")
    triangle.add_edge("B", "C")
    triangle.add_edge("C", "A")
    check("P7 triángulo con ciclos", silent(triangle.has_cycles), True)

    two = Undirected_graph()
    two.add_edge("A", "B")
    two.add_edge("C", "D")
    two.add_vertex("E")
    check("P7 componentes (A-B, C-D, E)", two.count_components(), 3)
    check("P7 bosque sin ciclos", silent(two.has_cycles), False)


def test_point_8():
    tree = Undirected_graph()
    tree.add_edge("A", "B")
    tree.add_edge("A", "C")
    tree.add_edge("C", "D")
    check("P8 árbol es árbol", silent(tree.is_tree), True)

    triangle = Undirected_graph()
    triangle.add_edge("A", "B")
    triangle.add_edge("B", "C")
    triangle.add_edge("C", "A")
    check("P8 triángulo no es árbol (ciclo)", silent(triangle.is_tree), False)

    two = Undirected_graph()
    two.add_edge("A", "B")
    two.add_edge("C", "D")
    check("P8 dos pedazos no es árbol (no conexo)", silent(two.is_tree), False)

    single = Undirected_graph()
    single.add_vertex("A")
    check("P8 un vértice solo es árbol", silent(single.is_tree), True)

    check("P8 grafo vacío no es árbol", silent(Undirected_graph().is_tree), False)


def test_point_9():
    two = Undirected_graph()
    two.add_edge("A", "B")
    two.add_edge("C", "D")
    two.add_vertex("E")
    check("P9 bosque (A-B, C-D, E)", silent(two.is_forest), True)

    tree = Undirected_graph()
    tree.add_edge("A", "B")
    tree.add_edge("B", "C")
    check("P9 un árbol también es bosque", silent(tree.is_forest), True)

    mixed = Undirected_graph()
    mixed.add_edge("A", "B")
    mixed.add_edge("B", "C")
    mixed.add_edge("C", "A")
    mixed.add_edge("X", "Y")
    check("P9 triángulo + X-Y no es bosque", silent(mixed.is_forest), False)


def demo():
    """Lo único que se imprime de verdad: el formato pedido por el enunciado."""
    for file_name in ["datos_grafo.txt", "arbol.txt", "bosque.txt"]:
        print(f"--- {file_name} ---")
        g = load_graph_from_file(file_name, Undirected_graph())
        g.is_connected()
        g.has_cycles()
        g.is_tree()
        g.is_forest()


def main():
    tests = [test_point_3, test_point_4, test_point_5,
             test_point_6, test_point_7, test_point_8, test_point_9]
    for test in tests:
        test()

    demo()

    if failures:
        print("\nPruebas fallidas:")
        for failure in failures:
            print("  -", failure)


if __name__ == "__main__":
    main()