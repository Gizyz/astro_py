import pygame
import sys
import math
from pygame.locals import * 


pygame.init()

HEIGHT = 450
WIDTH = 400
ACC = 1.5
FRIC = -0.2
ROTACC = 0.6
ROTFRIC = -0.1
FPS = 60

vec = pygame.math.Vector2

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game")