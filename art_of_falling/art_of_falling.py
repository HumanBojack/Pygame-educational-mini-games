from multiprocessing import Condition
from re import S
import pygame
import random
import json
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
    self.difficulty = 1.0 # est-ce que c'est encore utile ?

    self.load_wip_words()
    self.load_wig_words()
    self.wig_font = pygame.font.Font("assets/coders_crux.ttf", 60)

    self.all_words = pygame.sprite.Group()
    self.previous_games = -1
    self.instantiate_gamemode()


  def update(self):
    for word in self.check_collision(self.player, self.all_words):
      if word.is_correct:
        self.player.score += 10  
      else:
        self.player.lose_health()
      # delete and recreate words when there is a collision
      self.all_words = pygame.sprite.Group()
      # Select the next gamemode
      self.instantiate_gamemode()

    # Display the background and the player (at a given position)
    self.set_background(self.background)
    self.screen.blit(self.player.image, self.player.positions[self.player.position])

    for word in self.all_words:
      word.forward()
    self.all_words.draw(self.screen)

    if self.gamemode == "which_is_good":
      print(self.wig_question.get_rect().w)
      position_x = (640 - self.wig_question.get_rect().w) / 2
      self.screen.blit(self.wig_question, (position_x, 425))
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

    return words, index

  def which_is_python(self):
    words, index = self.wip_select_word()
    self.createwords(words, index)

  def wig_select_word(self):
    level = random.choice(self.wig_words)
    # self.wig_words.remove(level) => recharger load_game_mode()
    question, words = level
    good_answer = words[0]

    random.shuffle(words)
    index = words.index(good_answer)

    return words, index, question

  def which_is_good(self):
    words, index, question = self.wig_select_word()
    self.createwords(words, index)
    # display question
    self.wig_question = self.wig_font.render(question, True, (0,0,0))
    
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
      self.which_is_good()
    elif self.gamemode == "which_is_python":
      self.which_is_python()

  def load_wig_words(self):
    with open("assets/wig_words.json") as f:
      self.wig_words = list(json.load(f))

  def load_wip_words(self):
    with open("assets/wip_good.json") as f:
      self.wip_good = list(json.load(f))
    with open("assets/wip_wrong.json") as f:
      self.wip_wrong = list(json.load(f))
