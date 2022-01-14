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
        self.tmx_data = pytmx.util_pygame.load_pygame('./assets/overworld_assets/map.tmx')
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
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
        


        #définir une liste qui va stocker les rectangles de collision
        self.walls = []

        for obj in self.tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    def run(self):
    # Boucle du jeu
    
        clock = pygame.time.Clock()
    
        running = True
        while running:
            self.handle_input()
            self.group.update()
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
        clock.tick(60)

        pygame.quit()

    def update(self):
        self.group.update()

        #vérification collision
        # for sprite in self.group.sprites():
            # if sprite.feet.collidelist(self.walls) > -1:
                # sprite.move_back()