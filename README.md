# Proyect_grafos

Importante: Para ejecutarlo, escribir uv run python main.py ruta/al/archivo.txt

Implementamos dos formas para hacer los grafos:
1.Lista de adyacencia con objetos 
2.Matriz de adyacencia (grafo dirigido con pesos)

Lista de adyacencia con objetos (grafo no dirigido)

Usamos esta forma porque venimos de Programacion orientada a objetos en lenguaje de C++ y ya habiamos aprendido a crear clases y objetos, así que hicimos una clase Vertex, una Edge y una Undirected_graph. Cada vértice guarda la lista de sus vecinos, es algo como parecido a los punteros, por lo que se nos hizo más fácil de entender. También gasta menos memoria, porque solo guarda las conexiones que sí existen y no toda una tabla llena de espacios vacíos. Además nos parecio como mas práctica para recorrer el grafo y para contar las aristas que necesitamos al detectar ciclos.

Matriz de adyacencia (grafo dirigido con pesos)

Usamos la matriz porque era un tema que ya habiamos mirado en Progrmacion Imperativa en python y es parecida a los arreglos de dos dimensiones que vimos en C++, y se adapta bien a un grafo dirigido: matrix[i][j] es la aristas de i a j, y matrix[j][i] es otro distinto, tambien es como mas rapida para consultar por ejemplo para saber si existe un arista o cuánto pesa, vamos directo sin recorrer listas ni buscar.

En general el proyecto nos fue bien y logramos que todos los puntos funcionaran, pero tuvimos varios problemas en el desarrollo. por ejemplo utilizando Git y GitHub nos enredamos con algunos comandos, sobre todo al subir los cambios y al sincronizar los archivos entre los dos, y tuvimos que averiguar algunos comandos necesarios. También se nos olvidó parte de la sintaxis de Python: por ejemplo, escribimos el constructor como _init_ con un solo guion bajo en vez de __init__, y escribimos mal agunas variables,etc. 

Otro problema fue la organización del proyecto al ejecutar main.py nos salió el error de que no encontraba el módulo proyecto_grafos, porque el paquete estaba dentro de la carpeta src, y además la terminal PowerShell no nos dejaba activar el entorno virtual. Hicimos tambien varias pruebas de las funciones. 

