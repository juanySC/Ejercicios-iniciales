import matplotlib.pyplot as plt  # Importamos la libreria para crear graficos 2D
from itertools import combinations  # Para generar combinaciones de conjuntos
import matplotlib.patches as patches

# Funcion para pedir al usuario que ingrese los elementos de un conjunto
def ingresar_elementos_conjunto(conjunto_numero):
    # Pedimos los elementos de un conjunto en una sola linea, separados por comas o espacios
    while True:
        entrada = input(f"Ingresa los elementos del Conjunto {conjunto_numero}, separados por comas o espacios: ")
        # Limpiamos la entrada y la separamos en una lista de elementos
        elementos = set(entrada.replace(",", " ").split())  # Usamos un set para evitar duplicados
        if len(elementos) > 15:
            print("Has ingresado mas de 15 elementos, intenta nuevamente.")
        else:
            return elementos

# Funcion para dibujar los circulos y las intersecciones
def dibujar_circulos_con_intersecciones(conjuntos):
    # Creamos una figura y un eje donde vamos a dibujar los circulos (es la ventana que se crea)
    fig, ax = plt.subplots(figsize=(12, 10))  # Ancho 12, alto 10 pulgadas

    # Lista de colores para diferenciar los conjuntos visualmente
    colores = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'cyan', 'magenta', 'gray', 'gold']

    # Posiciones basicas (x, y) para ubicar hasta 10 circulos sin que se empalmen mucho
    # Los colocamos en una cuadricula de 5 columnas
    posiciones = [(i % 5, i // 5) for i in range(10)]

    # Dibujamos los circulos con los elementos
    for i, conjunto in enumerate(conjuntos):
        circ = plt.Circle(
            (posiciones[i][0] * 4, posiciones[i][1] * 4),  # posicion del centro del circulo
            3.5,                                               # radio
            color=colores[i],                                  # color del circulo
            alpha=0.4,                                          # transparencia
        )
        ax.add_patch(circ)
        # Escribimos los elementos dentro del circulo
        for elem in conjunto:
            ax.text(posiciones[i][0] * 4, posiciones[i][1] * 4, elem, fontsize=12, ha='center', va='center')

    # Establecemos los limites del area visible del grafico en X e Y
    ax.set_xlim(-3.5, 18)  # eje X
    ax.set_ylim(-4.5, 9)   # eje Y
    ax.set_aspect('equal')  # Para que los circulos no se deformen

    # Calculamos las intersecciones entre los conjuntos
    intersecciones = {}
    for r in range(2, len(conjuntos) + 1):
        for combinacion in combinations(range(len(conjuntos)), r):
            inter = set(conjuntos[combinacion[0]])  # Empezamos con el primer conjunto
            for idx in combinacion[1:]:
                inter &= set(conjuntos[idx])  # Interseccion entre los conjuntos
            if inter:
                intersecciones[combinacion] = inter

    # Dibujamos las intersecciones entre los conjuntos
    for key, inter in intersecciones.items():
        # Calculamos el centro de la interseccion de los conjuntos
        centers = [posiciones[i] for i in key]
        avg_x = sum([center[0] for center in centers]) / len(centers)
        avg_y = sum([center[1] for center in centers]) / len(centers)

        # Dibujamos los elementos de la interseccion en el centro de las areas de interseccion
        for elem in inter:
            ax.text(avg_x * 4, avg_y * 4, elem, fontsize=12, ha='center', va='center')

    # Mostramos el grafico
    plt.title("Diagrama de Venn con Intersecciones")
    plt.show()

# Funcion principal que gestiona la entrada del usuario
def gestionar_conjuntos():
    num_conjuntos = int(input("Cuantos conjuntos deseas ingresar? (maximo 10): "))
    
    # Verificamos que el numero de conjuntos este entre 1 y 10
    if num_conjuntos < 1 or num_conjuntos > 10:
        print("El numero de conjuntos debe estar entre 1 y 10.")
        return

    conjuntos = []
    for i in range(1, num_conjuntos + 1):
        conjunto = ingresar_elementos_conjunto(i)
        conjuntos.append(conjunto)
    
    # Dibujamos los circulos y las intersecciones
    dibujar_circulos_con_intersecciones(conjuntos)

# Llamamos a la funcion principal
gestionar_conjuntos()
