from multiprocessing import Condition
from re import S
import pygame
import random
from player import Player
from word import Word
from menu import Menu

class ArtOfFalling:

  def __init__(self, screen):
    # Load the background and initiate the player
    self.background = pygame.image.load("assets/background.png")
    self.background = pygame.transform.scale(self.background, (640,480))
    self.screen = screen
    self.isplaying = False
    self.isrunning = True
    self.player = Player(self)
    self.difficulty = 1.0
    self.wip_good = ['print("hello world")', 'def nom():', 'n = 0', 'Class nom():', 'array.append("hello")']
    self.wip_wrong = ['display("hello world)', "funct nom():", "n = 0;", "mauvais", "pasbon", "no", "pasça", "tjrspas", "try again", "game over", "end"]
    self.previous_games = -1

    self.all_words = pygame.sprite.Group()
    self.instantiate_gamemode()


  def update(self):
    # Display the background and the player (at a given position)
    self.set_background(self.background)
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

      self.instantiate_gamemode()

    pygame.display.flip()

  def menu(self):
    menu = Menu(self)
    while self.isrunning and not self.isplaying:

      menu.update()

  def set_background(self, background):
    self.screen.blit(background, (0, 0))

  def createwords(self):
    self.all_words.add(Word(self, 0, "salut"))
    self.all_words.add(Word(self, 1, "print(\"hello\")", True))
    self.all_words.add(Word(self, 2, "print(hello)"))
  
  def check_collision(self, sprite, group):
    return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
  
  def gameover(self, score = None):
    print ("perdu")
    self.isplaying = False
  
  def wip_selct_word(self):
    firstword = random.choice(self.wip_good)
    secondword = random.choice(self.wip_wrong)
    thridword = random.choice(self.wip_wrong)

    list = [firstword, secondword, thridword]
    random.shuffle(list)
    list.index(firstword)
    condition1 = False
    condition2 = False
    condition3 = False
    if list[0] == firstword:
      condition1 = True
    if list[1] == firstword:
        condition2 = True
    if list[2] == firstword:
      condition3 = True


    self.all_words.add(Word(self, 0, list[0], condition1))
    self.all_words.add(Word(self, 1, list[1], condition2))
    self.all_words.add(Word(self, 2, list[2], condition3))

  def which_is_python(self):
    self.wip_selct_word

  def gamemode_selector(self):
    if self.previous_games == -1:
      self.gamemode = random.choice(["which_is_good", "which_is_python"])
    elif self.previous_games == 5:
      self.previous_games = 0
      self.gamemode = ("which_is_good", "which_is_python")[self.gamemode == "which_is_good"]

  def instantiate_gamemode(self):
    self.gamemode_selector()
    print(self.gamemode)

    self.previous_games += 1
    if self.gamemode == "which_is_good":
      self.createwords()
    elif self.gamemode == "which_is_python":
      pass
    ##maj
