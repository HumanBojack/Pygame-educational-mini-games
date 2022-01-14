import pygame

class Player(pygame.sprite.Sprite):

  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("assets/player.png")
    self.rect = self.image.get_rect()
    self.positions = [(30,0),(30,200),(30,400)]
    
    self.position = 1
    self.default_pos = 1

  
