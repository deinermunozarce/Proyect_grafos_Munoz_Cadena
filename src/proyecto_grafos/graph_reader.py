def load_graph_from_file(path, graph):
    # utf-8-sig lee UTF-8 con o sin BOM
    #Ayuda de la IA para que funcione con cualquier tipo de archivo de texto
    with open(path, "r", encoding="utf-8-sig") as file:
        text = file.read()

    lines = text.split("\n")

    for number in range(len(lines)):
        line = lines[number]
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
        parts.append(current)

        # Validación: deben ser exactamente 3 campos
        if len(parts) != 3:
            raise ValueError(f"Línea {number + 1}: se esperaba source,target,weight")

        source = parts[0].strip()
        target = parts[1].strip()

        try:
            weight = float(parts[2])
        except ValueError:
            raise ValueError(f"Línea {number + 1}: el peso '{parts[2].strip()}' no es un número")

        if weight == int(weight):
            weight = int(weight)  # mantén el 3 como 3, no como 3.0

        graph.add_edge(source, target, weight)

    return graph
