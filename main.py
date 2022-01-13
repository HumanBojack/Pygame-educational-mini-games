import pygame

pygame.init()

#generate game display
pygame.display.set_caption("Simplon Python Quest")
screen = pygame.display.set_mode((1600,900))


running = True
#game loop

while running:
    for event in pygame.event.get():
        # Game loop end => player quit the game
        if event.type == pygame.QUIT:
            running = False