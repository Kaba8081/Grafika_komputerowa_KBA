import pygame
import math

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")

# deklarowanie kolorów
POMARANCZOWY = (255, 165, 0)

# deklarowanie punktów wielokąta
num_sides = 11
radius = 150
center = (300, 300)

transformations = {
    pygame.K_1: (center[0], center[1], 0, 0.5, 0.5, 0, 0),
    pygame.K_2: (center[0], center[1], 45, 1, 1, 0, 0), 
    pygame.K_3: (center[0], center[1], 180, 0.5, 0.75, 0, 0),
    pygame.K_4: (center[0], center[1], -30, 1, 1, 0.3, 0),
    pygame.K_5: (center[0], 50, 0, 1, 0.5, 0, 0),
    pygame.K_6: (center[0], center[1], 90, 1, 1, 0, -0.5),
    pygame.K_7: (center[0], center[1], 180, 0.5, 0.75, 0, 0),  
    pygame.K_8: (center[0] - 100, center[1] + 100, -45, 1, 1, 0, 0), 
    pygame.K_9: (600 - 100, center[1], 180, 1, 1, 0.3, 0)
}
curr_transform = transformations[pygame.K_1]

def draw_polygon(x, y, angle, scale_x, scale_y, skew_x, skew_y):
    points = []
    for i in range(num_sides):
        theta = (2 * math.pi * i / num_sides) + math.radians(angle)
        px = x + int(radius * scale_x * math.cos(theta))
        py = y + int(radius * scale_y * math.sin(theta))

        px += int((py - y) * skew_x)
        py += int((px - x) * skew_y)

        points.append((px, py))

    pygame.draw.polygon(screen, POMARANCZOWY, points)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key in transformations:
            curr_transform = transformations[event.key]

    screen.fill((0, 0, 0))
    draw_polygon(*curr_transform)
    pygame.display.flip()
