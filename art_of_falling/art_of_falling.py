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
    self.difficulty = 1.0

    self.load_wip_words()
    self.load_wig_words()
    self.wig_font = pygame.font.Font("assets/coders_crux.ttf", 80)
    self.hud_font = pygame.font.Font("assets/coders_crux.ttf", 30)

    self.all_words = pygame.sprite.Group()
    self.rounds = -1
    self.execute_gamemode()


  def update(self):
    for word in self.check_collision(self.player, self.all_words):
      if word.is_correct:
        self.player.score += 10  
      else:
        self.player.lose_health()
      # delete and recreate words when there is a collision
      self.all_words = pygame.sprite.Group()
      # Select the next gamemode
      self.execute_gamemode()
   
    # Display the background and the player (at a given position)
    self.set_background(self.background)
    self.screen.blit(self.player.image, self.player.positions[self.player.position])

    for word in self.all_words:
      word.forward()
    self.all_words.draw(self.screen)

    if self.gamemode == "which_is_good":
      position_x = (640 - self.wig_question.get_rect().w) / 2
      self.screen.blit(self.wig_question, (position_x, 420))
    self.update_score()
    self.update_health()
    pygame.display.flip()

  def update_score(self):
    scoredraw = f"Score: {int(self.player.score * self.difficulty)} (x{self.difficulty})"
    scoredraw = self.hud_font.render(scoredraw, True, (192,255,255))
    self.screen.blit(scoredraw, (10, 462)) # (50, 420) (420, 30) (10, 462) (425, 10)
  
  def update_health(self):
    health_display = f"{self.player.health} life remaining"
    health_display = self.hud_font.render(health_display, True, (0,0,0))
    self.screen.blit(health_display, (440,10))

  def menu(self):
    menu = Menu(self)
    while self.isrunning and not self.isplaying:
      menu.update()

  def set_background(self, background):
    self.screen.blit(background, (0, 0))
  
  def check_collision(self, sprite, group):
    return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
  
  def gameover(self, score = None):
    self.isplaying = False

  def createwords(self, words, index):
    for i in range(3):
      self.all_words.add(Word(self, i, words[i], i == index))
  
  def wip_select_word(self):
    firstword = random.choice(self.wip_good)
    secondword = random.choice(self.wip_wrong)
    thirdword = random.choice(self.wip_wrong)

    words = [firstword, secondword, thirdword]
    random.shuffle(words)
    index = words.index(firstword)

    return words, index

  def which_is_python(self):
    words, index = self.wip_select_word()
    self.createwords(words, index)

  def wig_select_word(self):
    level = random.choice(self.wig_words)

    self.wig_words.remove(level)
    if not self.wig_words:
      print("reloading")
      self.load_wig_words()

    question = level["question"]
    words = level["values"]
    good_answer = level["good"]

    random.shuffle(words)
    index = words.index(good_answer)

    return words, index, question

  def which_is_good(self):
    words, index, question = self.wig_select_word()
    self.createwords(words, index)
    # display question
    self.wig_question = self.wig_font.render(question, True, (0,0,0))
    
  def gamemode_selector(self):
    if self.rounds == -1:
      self.rounds = 1
      self.gamemode = random.choice(["which_is_good", "which_is_python"])
    elif self.rounds % 5 == 0:
      self.rounds = 0
      self.gamemode = ("which_is_good", "which_is_python")[self.gamemode == "which_is_good"]

  def execute_gamemode(self):
    self.gamemode_selector()

    self.rounds += 1
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
