from re import S
import pygame
from player import Player
from word import Word

class ArtOfFalling:

  def __init__(self, screen):
    # Load the background and initiate the player
    self.background = pygame.image.load("assets/background.png")
    self.screen = screen
    self.player = Player()

    self.all_words = pygame.sprite.Group()


  def update(self):
    # Display the background and the player (at a given position)
    self.set_background(self.background, self.screen)
    self.screen.blit(self.player.image, self.player.positions[self.player.position])

    self.all_words.add(Word(self, 0))
    self.all_words.add(Word(self, 1))
    self.all_words.add(Word(self, 2))

    self.all_words.draw(self.screen)

    pygame.display.flip()


  def set_background(self, background, screen):
    screen.blit(background, (0,0))