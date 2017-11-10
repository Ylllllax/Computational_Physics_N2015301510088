import pygame,sys
from pygame.locals import *
import random

def choice(seq, prob):
    p = random.random()
    for i in range(len(seq)):
        if sum(prob[:i]) < p < sum(prob[:i+1]):
            return seq[i]

class PlayerSprite(pygame.sprite.Sprite):
    speed = 3
    
    def __init__(self): 
        super().__init__()
        self.image = pygame.image.load('bird.jpg').convert() 
        self.image.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.image.get_rect()
        
    def update(self, key):
        if key[K_UP]:
            self.rect.move_ip(0, -self.speed)
        if key[K_DOWN]:
            self.rect.move_ip(0, self.speed)
        if key[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if key[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600

class EnemySprite(pygame.sprite.Sprite):
    speed = choice([1,1,1], [0.5, 0.4, 0.1])
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('guan.jpg').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(center=(820, random.randint(0, 600)))
        self.speed = random.randint(3, 7)

    def update(self):
        self.rect.move_ip(-self.speed, 0) 
        if self.rect.right < 0:
            self.kill() 

class BackgroundSprite(pygame.sprite.Sprite):

    def __init__(self, size):
        super().__init__()
        self.image = pygame.image.load('background.jpg') 
        self.rect = pygame.Rect(0, 0, *size)

    def update(self):
        pass
        

class Game():

    def __init__(self):
        pygame.init()

        self.size = self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode(self.size)

        pygame.display.set_caption("super bird!")
        

        self.ADDENEMY = pygame.USEREVENT + 1     
        pygame.time.set_timer(self.ADDENEMY, 250) 
        self.ADDCLOUD = pygame.USEREVENT + 2        
        pygame.time.set_timer(self.ADDCLOUD, 1000)

        self.background = BackgroundSprite(self.size)
        self.player = PlayerSprite()

        self.enemies = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        
        self.all_sprites.add(self.player)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()       
                elif event.type == KEYDOWN:           
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()                
                elif event.type == self.ADDENEMY:
                    new_enemy = EnemySprite()
                    self.enemies.add(new_enemy)
                    self.all_sprites.add(new_enemy)


            self.screen.blit(self.background.image, self.background.rect)
            
            key = pygame.key.get_pressed()
            self.player.update(key)
            self.enemies.update()

            for sprite in self.all_sprites:
                self.screen.blit(sprite.image, sprite.rect)
                
            if pygame.sprite.spritecollideany(self.player, self.enemies):
                self.player.kill()
                self.gameover = pygame.image.load('gameover.jpg')
                self.screen.blit(self.gameover, (0, 0))  
            
            pygame.display.flip()        

if __name__ == '__main__':
    Game().run()
