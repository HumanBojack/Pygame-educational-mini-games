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
    self.createword()


  def update(self):
    # Display the background and the player (at a given position)
    self.set_background(self.background, self.screen)
    self.screen.blit(self.player.image, self.player.positions[self.player.position])

    
    for word in self.all_words:
      word.forward()
    self.all_words.draw(self.screen)
    


    pygame.display.flip()


  def set_background(self, background, screen):
    screen.blit(background, (0,0))

  def createword(self):
    self.all_words.add(Word(self, 0, "salut"))
    self.all_words.add(Word(self, 1, "print(\"hello\")"))
    self.all_words.add(Word(self, 2, "print(hello)"))
  