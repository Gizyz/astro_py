from init import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((10, 20))
        self.surf.fill((128,255,40))
        self.surf.set_colorkey("BLACK")
        self.rect = self.surf.get_rect(center=(WIDTH/2, HEIGHT/2))

        self.rot_surf = self.surf

        self.pos = vec((WIDTH/2, HEIGHT/2))
        self.vel = 0        
        self.acc = 0
        self.accxy = vec(0,0)

        self.rot = 0
        self.rotvel = 0
        self.rotacc = 0

        

    def move(self):
        self.acc = 0
        self.accxy = vec(0,0)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_DOWN]:
            self.acc = ACC
        if pressed_keys[K_UP]:
            self.acc = -ACC

        if pygame.KEYUP:
            self.rotacc = 0
        if pressed_keys[K_LEFT]:
            self.rotacc = -ROTACC
        if pressed_keys[K_RIGHT]:
            self.rotacc = ROTACC
        



        (self.acc, self.vel) = accelerator(self.acc, self.vel, FRIC)
        self.acc = self.vel + round(self.acc,2) * 0.5

        (self.rotacc, self.rotvel) = accelerator(self.rotacc, self.rotvel, ROTFRIC)
        self.rotacc = self.rotvel + round(self.rotacc,2) * 0.5
        self.rot += self.rotacc
        self.rot %= 360

        (self.accxy.x, self.accxy.y) = xy_from_angle(self.acc, self.rot) 
        print("x_:",round(self.accxy.x,2), "y_:",round(self.accxy.x,2))
        
        self.pos.x += self.accxy.x
        self.pos.y += self.accxy.y

        print(round(self.rot,2))

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.y > HEIGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = HEIGHT

        self.saved_center=self.rect.center

        self.rot_surf = pygame.transform.rotate(self.surf, -self.rot)
        self.rect = self.surf.get_rect()

        self.rect.midbottom = self.pos


def accelerator(acceleration, velocity, friction):
    acceleration += velocity * friction
    velocity += acceleration
    return (acceleration, velocity)

def xy_from_angle(hyphotenus, angle):
    x = hyphotenus * math.cos(math.radians(angle))
    y = math.tan(math.radians(angle))*x
    return (x,y)

