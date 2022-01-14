from re import S
import pygame
from player import Player

class ArtOfFalling:

  def __init__(self, screen):
    # Load the background and initiate the player
    self.background = pygame.image.load("assets/background.png")
    self.screen = screen
    self.player = Player()


  def update(self):
    # Display the background and the player (at a given position)
    self.set_background(self.background, self.screen)
    self.screen.blit(self.player.image, self.player.positions[self.player.position])
    pygame.display.flip()


  def set_background(self, background, screen):
    screen.blit(background, (0,0))