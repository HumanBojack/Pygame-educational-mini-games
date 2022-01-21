import pygame

class Menu():

  def __init__(self, game):
    self.game = game
    self.selected_difficulty = 1.0
    self.displayed_difficulty = "Normal"

    self.font = pygame.font.Font("assets/coders_crux.ttf", 60)
    self.background = game.background
    
    # self.image = self.font.render(text, True, (0,0,0))
    # self.rect = self.image.get_rect()


  def update(self):
    self.check_keys()
    self.game.set_background(self.background)

    title = self.font.render(self.displayed_difficulty, True, (255,0,0))
    self.game.screen.blit(title, (50,50))

    pygame.display.flip()
    

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
    self.displayed_difficulty = ("Normal", "Hardcore")[self.selected_difficulty == 1.5]