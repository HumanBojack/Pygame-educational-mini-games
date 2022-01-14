import pygame
import pytmx
import pyscroll
from pygame import key
# from player import Player

class Game:
    def __init__(self):
        # Créer la fenêtre du jeu
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Pyquest")

        # charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame('./assets/overworld_assets/map.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1

        #générer un joueur
        # self.player = Player()

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer = 1)

        #définir une liste qui va stocker les rectangles de collision
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    def run(self):
    # Boucle du jeu
        running = True
        while running:

            # self.player.save_location()
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()

    def update(self):
        self.group.update()

        #vérification collision
        # for sprite in self.group.sprites():
            # if sprite.feet.collidelist(self.walls) > -1:
                # sprite.move_back()