from init import *
from player_controller import *

P1 = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    displaysurface.fill((0,0,0))

    for entity in all_sprites:
        displaysurface.blit(entity.rot_surf, entity.rect)
    
    P1.move()

    pygame.display.update()
    FramePerSec.tick(FPS)