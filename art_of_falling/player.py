import pygame

class Player(pygame.sprite.Sprite):

  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("assets/player.png")
    self.rect = self.image.get_rect()
    self.rect.x = 30
    self.rect.y = 0
