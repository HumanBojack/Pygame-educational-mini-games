import pygame

class Character(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 100
        self.image = pygame.image.load('assets/character.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def move_right(self):
        self.rect.x += self.velocity 

    def move_left(self):
        self.rect.x -= self.velocity 

    def move_up(self):
        self.rect.y += self.velocity 

    def move_down(self):
        self.rect.y -= self.velocity  