import pygame
import math
import random

# Inicialización
pygame.init()
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Venn Dinámico")
font = pygame.font.SysFont("Arial", 18)

# Cantidad de circulos
num_conjuntos = 10
radio = 100

# Función para colores aleatorios semi-transparentes
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 100)

# Calcular posiciones en círculo
def generar_posiciones(n, centro_x, centro_y, radio_circulo):
    posiciones = []
    angulo = 2 * math.pi / n
    for i in range(n):
        x = centro_x + int(math.cos(i * angulo) * radio_circulo)
        y = centro_y + int(math.sin(i * angulo) * radio_circulo)
        posiciones.append((x, y))
    return posiciones

# Preparar conjuntos
colores = [random_color() for _ in range(num_conjuntos)]
posiciones = generar_posiciones(num_conjuntos, WIDTH // 2, HEIGHT // 2, 250)

# Bucle principal
running = True
while running:
    screen.fill((255, 255, 255))

    for i in range(num_conjuntos):
        surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        pygame.draw.circle(surface, colores[i], posiciones[i], radio)
        screen.blit(surface, (0, 0))
        # Etiqueta
        label = font.render(f"Conjunto {chr(65+i)}", True, (0, 0, 0))
        screen.blit(label, (posiciones[i][0]-20, posiciones[i][1]-10))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
