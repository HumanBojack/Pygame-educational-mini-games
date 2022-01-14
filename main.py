import pygame
from game import Game

pygame.init()

#generate game display
pygame.display.set_caption("Simplon Python Quest")
screen = pygame.display.set_mode((1600,900))

running = True

#game loop

while running:
    game=Game()
    #display the characther of the player
    screen.blit(game.character.image, game.character.rect)
    #mettre a jour l'écran
    pygame.display.flip()

    for event in pygame.event.get():
        # Game loop end => player quit the game
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif  event.type == pygame.KEYDOWN:
            #move character
            if event.key == pygame.K_RIGHT:
                game.character.move_right()
            if event.key == pygame.K_LEFT:
                game.character.move_left()
            if event.key == pygame.K_UP:
                game.character.move_up()
            if event.key == pygame.K_DOWN:
                game.character.move_down()


