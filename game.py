# File: main.py
# File: game.py
# this is a simple game where you dodge  falling asteroids
# you can move left and right using the arrow keys
import pygame # type: ignore
import time
import random
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("space dodge")

