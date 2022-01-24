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
    self.wip_wrong = ['DISPLAY "hello world"', "funct nom():", "n = 0;", "mauvais", "pasbon", "no", "pasça", "tjrspas", "try again", "game over", "end"]
    self.font = pygame.font.Font("assets/coders_crux.ttf", 30)
    self.all_words = pygame.sprite.Group()
    self.previous_games = -1
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
   
    scoredraw = str(int (self.player.score * self.difficulty))
    scoredraw = "score : " + scoredraw
    scoredraw = self.font.render(scoredraw, True, (255,255,255))
    self.screen.blit(scoredraw, (50, 420))

    pygame.display.flip()

  def menu(self):
    menu = Menu(self)
    while self.isrunning and not self.isplaying:
      menu.update()

  def set_background(self, background):
    self.screen.blit(background, (0, 0))
  
  def check_collision(self, sprite, group):
    return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
  
  def gameover(self, score = None):
    print ("perdu")
    self.isplaying = False

  def createwords(self, words, index):
    for i in range(3):
      self.all_words.add(Word(self, i, words[i], i == index))
  
  def wip_select_word(self):
    firstword = random.choice(self.wip_good)
    secondword = random.choice(self.wip_wrong)
    thridword = random.choice(self.wip_wrong)

    words = [firstword, secondword, thridword]
    random.shuffle(words)
    index = words.index(firstword)
    print(index)

    return words, index

  def which_is_python(self):
    words, index = self.wip_select_word()
    self.createwords(words, index)

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
      self.which_is_python()
    elif self.gamemode == "which_is_python":
      pass
