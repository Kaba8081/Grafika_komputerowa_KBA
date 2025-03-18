import pygame
import math

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")

# wariant numer 2
ZIELONY = (52, 235, 52)
triangles = [
    [(200, 200), (400, 200), (300, 300)],
    [(400, 200), (400, 400), (300, 300)],
    [(200, 200), (300, 300), (200, 400)]
]

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))

    for triangle_vert in triangles:
        pygame.draw.polygon(screen, ZIELONY, triangle_vert)

    pygame.display.flip()
