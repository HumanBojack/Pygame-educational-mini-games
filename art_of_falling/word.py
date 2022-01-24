
import pygame

class Word(pygame.sprite.Sprite):

  def __init__(self, game, index, text, is_correct = False ):
    super().__init__()
    self.game = game
    self.font = pygame.font.Font("assets/coders_crux.ttf", 60)
    self.image = self.font.render(text, True, (0,0,0))
    self.rect = self.image.get_rect()
    self.rect.x = 700
    self.rect.y = self.game.player.positions[index][1] + self.rect.h
    self.velocity = 4
    self.is_correct = is_correct

  def forward(self):
    self.rect.x -= self.velocity + (self.game.difficulty * ((self.game.rounds + 1) / 8)) # Increase the dividing number to reduce the difficulty
    if self.rect.x < 0:
      self.remove()