import pygame
import sys
from pygame.locals import * 


pygame.init()

HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
ROTACC = 0.9
ROTFRIC = -0.1
FPS = 60

vec = pygame.math.Vector2

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game")