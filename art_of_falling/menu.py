
import pygame

class Menu():

  def __init__(self, game):
    self.game = game
    self.selected_difficulty = 1.0
    self.displayed_difficulty = "Normal"

    self.font = pygame.font.Font("assets/coders_crux.ttf", 60)
    self.background = game.background


  def update(self):
    self.check_keys()
    self.game.set_background(self.background)

    hard_color = ((128,128,128), (255,0,0))[self.selected_difficulty == 1.5]
    nrml_color = ((128,128,128), (255,0,0))[self.selected_difficulty == 1.0]
    hard = self.font.render("Hard", True, hard_color)
    normal = self.font.render("Normal", True, nrml_color)
    # normal_x = screensize[0]/2
    # normal_y = screensize[1]/2
    screensize_ = self.game.screen.get_rect()
    print(screensize_[2])

    #place of menu
    normal_police = normal.get_rect()
    hard_police = hard.get_rect()

    normal_x = (screensize_[2] - normal_police[2] - hard_police[2] - (hard_police[2]/2))/2
    hard_x   = (screensize_[2] - hard_police[2] + normal_police[2])/2
    normal_y = ((screensize_[3] - normal_police[3] )/2) - hard_police[3]
    hard_y   = ((screensize_[3] - normal_police[3] )/2) - hard_police[3]

    self.game.screen.blit(normal, (normal_x,normal_y))
    self.game.screen.blit(hard, (hard_x, hard_y))

    pygame.display.flip()
    

  def check_keys(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        self.game.isrunning = False
        
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
          self.change_difficulty()
        elif event.key == pygame.K_RETURN:
          self.game.isplaying = True
          self.game.player.reset()
          self.game.difficulty = self.selected_difficulty

  def change_difficulty(self):
    self.selected_difficulty = (1.0, 1.5)[self.selected_difficulty == 1.0]
    