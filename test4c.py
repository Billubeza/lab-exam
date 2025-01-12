import pygame
import sys

pygame.init()

width, height = 600, 600
blue = (0, 0, 255)
white = (255, 255, 255)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Three Blue Triangles with White Triangle")

top_triangle = [(300, 100), (200, 300), (400, 300)]
bottom_left_triangle = [(200, 300), (100, 500), (300, 500)]
bottom_right_triangle = [(400, 300), (300, 500), (500, 500)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    pygame.draw.polygon(screen, blue, top_triangle)
    pygame.draw.polygon(screen, blue, bottom_left_triangle)
    pygame.draw.polygon(screen, blue, bottom_right_triangle)

    pygame.display.flip()

pygame.quit()
sys.exit()
