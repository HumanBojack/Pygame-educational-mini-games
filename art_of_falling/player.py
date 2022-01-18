import pygame

class Player(pygame.sprite.Sprite):

  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("assets/player.png")
    self.rect = self.image.get_rect()

    # This is all the available positions for the player, under than is an index
    self.positions = [(30,17.5),(30,126+17.5),(30,252+17.5)]
    self.position = 1
    self.rect.y = self.positions[self.position][1]

  def move(self, position):
    self.rect.y = self.positions[position][1]

  
