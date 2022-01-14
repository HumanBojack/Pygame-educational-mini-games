import pygame
from player import Player

class ArtOfFalling:

  def __init__(self, screen):
    self.background = pygame.image.load("assets/background.png")
    # self.set_background(self.background, screen)
    self.screen = screen
    self.player = Player()

  def update(self):
    self.set_background(self.background, self.screen)

    self.screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
    pygame.display.flip()

  def set_background(self, background, screen):
    screen.blit(background, (0,0))
