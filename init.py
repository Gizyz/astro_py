import pygame
import sys
import math
from pygame.locals import * 


pygame.init()

HEIGHT = 450
WIDTH = 400
ACC = 2
FRIC = -0.1
ROTACC = 0.3
ROTFRIC = -0.05
FPS = 60

vec = pygame.math.Vector2

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game")