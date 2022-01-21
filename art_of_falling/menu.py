import pygame

class Menu():

  def __init__(self, game):
      self.game = game
      self.selected_difficulty = 1.0


  def update(self):
    self.check_keys()
    

  def check_keys(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        self.game.isrunning = False
        
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
          self.change_difficulty()
        elif event.key == pygame.K_RETURN:
          print("enter !")
          self.game.isplaying = True
          self.game.player.reset()
          self.game.difficulty = self.selected_difficulty

  def change_difficulty(self):
    self.selected_difficulty = (1.0, 1.5)[self.selected_difficulty == 1.0]