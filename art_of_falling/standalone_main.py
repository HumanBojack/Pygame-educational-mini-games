import pygame
from art_of_falling import ArtOfFalling

pygame.init()

clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((640, 480))
game = ArtOfFalling(screen)

running = True
while running:

  game.update()

  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP and game.player.position > 0:
        game.player.position -= 1
      if event.key == pygame.K_DOWN and game.player.position < len(game.player.positions) - 1:
        game.player.position += 1
      if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        running = False