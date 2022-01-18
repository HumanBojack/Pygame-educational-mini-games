
import pygame

class Word(pygame.sprite.Sprite):

  def __init__(self, game, index, text, is_correct = False ):
    super().__init__()
    self.game = game
    self.font = pygame.font.Font("freesansbold.ttf", 32)
    self.image = self.font.render(text, True, (0,0,0))
    self.rect = self.image.get_rect()
    self.rect.x = 400
    self.rect.y = self.game.player.positions[index][1]
    self.velocity = 5
    self.is_correct = is_correct

  def forward(self):
    self.rect.x -= self.velocity
    if self.rect.x < 0:
      self.remove()
      