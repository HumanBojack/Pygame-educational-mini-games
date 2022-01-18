from re import S
import pygame
from player import Player
from word import Word

class ArtOfFalling:

  def __init__(self, screen):
    # Load the background and initiate the player
    self.background = pygame.image.load("assets/background.png")
    self.background = pygame.transform.scale(self.background, (640,480))
    self.screen = screen
    self.player = Player(self)
    

    self.all_words = pygame.sprite.Group()
    self.createwords()


  def update(self):
    # Display the background and the player (at a given position)
    self.set_background(self.background, self.screen)
    self.screen.blit(self.player.image, self.player.positions[self.player.position])

    
    for word in self.all_words:
      word.forward()
    self.all_words.draw(self.screen)
    
    for word in self.check_collision(self.player, self.all_words):
      if word.is_correct:
        self.player.score += 10  
      else:
        self.player.lose_health()
      # delete and recreate words when there is a collision
      self.all_words = pygame.sprite.Group()
      self.createwords()

    pygame.display.flip()


  def set_background(self, background, screen):
    screen.blit(background, (0,0))

  def createwords(self):
    self.all_words.add(Word(self, 0, "salut", True))
    self.all_words.add(Word(self, 1, "print(\"hello\")"))
    self.all_words.add(Word(self, 2, "print(hello)"))
  

  def check_collision(self, sprite, group):
    return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
  
  def gameover(self, score = None):
    print ("perdu")