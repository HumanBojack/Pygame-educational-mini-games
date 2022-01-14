import pygame
import pytmx
import pyscroll
from pygame import key
from character import Character
# from player import Player

class Game:
    def __init__(self):
    # Créer la fenêtre du jeu
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Pyquest")

    # charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame('map.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1

        #generate a player's character 
        self.character= Character(30,40)

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer = 1)
        self.group.add(self.character)
    
    def handle_input(self):
        """ This function asociate caps of key to character moves """
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.character.move_up()
        elif pressed[pygame.K_DOWN]:
            self.character.move_down()
        elif pressed[pygame.K_LEFT]:
            self.character.move_left()
        elif pressed[pygame.K_RIGHT]:
            self.character.move_right()
        


    def run(self):
    # Boucle du jeu
        running = True
        while running:
            self.handle_input()
            self.group.update()
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()