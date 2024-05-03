from init import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((128,255,40))
        self.surf.set_colorkey("BLACK")
        self.rect = self.surf.get_rect(center=(WIDTH/2, HEIGHT/2))

        self.rot_surf = self.surf

        self.pos = vec((WIDTH/2, HEIGHT/2))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

        self.rot = 0
        self.rotvel = 0
        self.rotacc = 0

        

    def move(self):
        self.acc = vec(0,0)
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_DOWN]:
            self.acc.y = ACC
        if pressed_keys[K_UP]:
            self.acc.y = -ACC

        if pressed_keys[K_LEFT]:
            self.rotacc = ROTACC
        if pressed_keys[K_RIGHT]:
            self.rotacc = -ROTACC

        self.acc.x += self.vel.x *FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rotacc += self.rotvel * ROTFRIC
        self.rotvel += self.rotacc
        self.rot += 10 * self.rotacc

        self.rot = round(self.rot) % 360
        print(self.rot)
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.y > HEIGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = HEIGHT

        self.saved_center=self.rect.center

        self.rot_surf = pygame.transform.rotate(self.surf, self.rot)
        self.rect = self.surf.get_rect()

        self.rect.midbottom = self.pos