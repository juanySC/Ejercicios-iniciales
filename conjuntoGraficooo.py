import pygame
import sys

# Ingresar elementos de los conjuntos
entrada_a = input("Ingrese los elementos del conjunto A (separados por coma): ")
entrada_b = input("Ingrese los elementos del conjunto B (separados por coma): ")

# Convertir a conjuntos (eliminar espacios y repetir elementos)
conjunto_a = set(e.strip() for e in entrada_a.split(','))
conjunto_b = set(e.strip() for e in entrada_b.split(','))
interseccion = conjunto_a & conjunto_b

# Inicializar pygame
pygame.init()

# Pantalla
ancho, alto = 600, 400
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Diagrama de Venn con datos")

# Fuente para texto
fuente = pygame.font.SysFont(None, 24)

# Colores
ROJO = (255, 0, 0, 120)
AZUL = (0, 0, 255, 120)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Superficies transparentes
circulo_rojo = pygame.Surface((300, 300), pygame.SRCALPHA)
circulo_azul = pygame.Surface((300, 300), pygame.SRCALPHA)

# Dibujar círculos
pygame.draw.circle(circulo_rojo, ROJO, (150, 150), 100)
pygame.draw.circle(circulo_azul, AZUL, (150, 150), 100)

# Función para escribir texto en pantalla
def escribir_elementos(elementos, pos_inicial):
    x, y = pos_inicial
    for elem in elementos:
        texto = fuente.render(str(elem), True, NEGRO)
        pantalla.blit(texto, (x, y))
        y += 20  # espacio entre líneas

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(BLANCO)

    # Dibujar círculos
    pantalla.blit(circulo_rojo, (150, 100))  # Conjunto A
    pantalla.blit(circulo_azul, (250, 100))  # Conjunto B

    # Escribir los elementos
    escribir_elementos(conjunto_a - interseccion, (160, 120))    # Solo A
    escribir_elementos(conjunto_b - interseccion, (360, 120))    # Solo B
    escribir_elementos(interseccion, (260, 150))                 # Intersección

    pygame.display.flip()
