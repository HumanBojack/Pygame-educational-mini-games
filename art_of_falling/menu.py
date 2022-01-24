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
    hard = self.font.render("hard", True, hard_color)
    normal = self.font.render("normal", True, nrml_color)

    self.game.screen.blit(normal, (50,50))
    self.game.screen.blit(hard, (250, 50))

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
    