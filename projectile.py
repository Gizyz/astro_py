from init import *


class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((10, 20))
        self.surf.fill((128,255,40))
        self.surf.set_colorkey("BLACK")
        self.rect = self.surf.get_rect(center=(WIDTH/2, HEIGHT/2))
        
        self.rot_surf = self.surf
        self.pos = vec()

        self.prjLife = 0

    def projectile_move(self, projectiles):
        for i in projectiles:
            rot = i[2]
            (x, y) = xy_from_angle(3, rot)
            i[0] += x
            i[1] += y
            
            if (i[0] > WIDTH or i[0] < 0 or i[1] > HEIGHT or i[1] < 0):
                print(i)
                print(WIDTH, HEIGHT)
                projectiles.pop(i[3])
                


