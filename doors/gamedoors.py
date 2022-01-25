import pygame
import pytmx
import pyscroll
from player import Player
from map import MapManager
from dialog import DialogBox

class Game:

    def __init__(self):

        #créer la fenêtre du jeu
        self.screen = pygame.display.set_mode((640,480)) #taille de la fenêtre
        pygame.display.set_caption("World of Simplon") #titre de la fenêtre

        #générer un joueur
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)
        self.dialog_box = DialogBox()

    
    def handle_input(self):
        "Récupère les touches enclenchées par le joueur"
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_up()
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
    
    def update(self):
        self.map_manager.update()

    def run(self):

        clock = pygame.time.Clock()

        #boucle du jeu
        running = True

        while running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            self.dialog_box.render(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.map_manager.check_npc_collisions(self.dialog_box)

            clock.tick(20)

        pygame.quit()