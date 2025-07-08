import pygame

# generle setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
runnning = True

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False



