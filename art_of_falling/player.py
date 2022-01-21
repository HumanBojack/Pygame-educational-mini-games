import pygame


class Player(pygame.sprite.Sprite):

  def __init__(self, game):
    super().__init__()
    self.image = pygame.image.load("assets/player.png")
    self.rect = self.image.get_rect()
    self.game = game
    # This is all the available positions for the player, under than is an index
    self.positions = [(30,17.5),(30,126+17.5),(30,252+17.5)]
    self.reset()
    

  def move(self, position):
    self.rect.y = self.positions[position][1]

  def lose_health(self):
    self.health -= 1 
    if self.health <= 0:
      self.game.gameover()

  def reset(self):
    self.position = 1
    self.rect.y = self.positions[self.position][1]
    self.health = 3
    self.score = 0

      


  
