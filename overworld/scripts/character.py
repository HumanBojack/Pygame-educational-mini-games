import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('overworld/assets/character.png')
        self.image = self.get_image(0,0)
        self.image.set_colorkey([0,0,0])
        self.rect =self.image.get_rect()
        self.position = [x,y]
        self.speed= 0.1

    def move_right(self):
        self.position[0] += self.speed
        
    def move_left(self):
        self.position[0] -= self.speed

    def move_up(self):
        self.position[1] -= self.speed
    
    def move_down(self):
        self.position[1] += self.speed

    def update(self):
        self.rect.topleft = self.position


    def get_image(self,x,y):
        """ get image from sprite sheet"""
        image = pygame.Surface([32,32])
        image.blit(self.sprite_sheet, (0,0), (x, y, 32, 32))
        return image