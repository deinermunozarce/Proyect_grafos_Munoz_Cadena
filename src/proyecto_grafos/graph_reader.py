def load_graph_from_file(path, graph):
    file = open(path, "r")
    text = file.read()          # leer todo como texto
    file.close()

    lines = text.split("\n")    # divide el texto en líneas

    for line in lines:
        if line.strip() == "":  # omitir líneas vacías
            continue

        # Divide la línea por comas, recorriéndola carácter por carácter.
        parts = []
        current = ""
        for character in line:
            if character == ",":
                parts.append(current)
                current = ""
            else:
                current = current + character
        parts.append(current)   # añade la última pieza

        source = parts[0].strip()
        target = parts[1].strip()
        weight = float(parts[2])
        if weight == int(weight):
            weight = int(weight)  # mantén el 3 como 3, no como 3.0

        graph.add_edge(source, target, weight)

    return graph