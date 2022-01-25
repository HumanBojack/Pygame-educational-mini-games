
import dataclasses
import pygame
import pytmx
import pyscroll
from dataclasses import dataclass
from player import NPC
import sys
import os

@dataclass
class Portal:
    from_world: str
    origin_point: str
    target_world: str
    teleport_point: str

@dataclass
class Map:
    name: str
    walls: list[pygame.Rect]
    group: pyscroll.PyscrollGroup
    tmx_data: pytmx.TiledMap
    portals: list[Portal]
    npcs: list[NPC]


class MapManager:

    def __init__(self,screen, player):
        self.maps = dict()
        self.screen = screen
        self.player = player
        self.current_map = "iamap"

        self.register_map("iamap", portals=[
            Portal(from_world="iamap", origin_point="entree_alpha", target_world="alpha", teleport_point="spawn_alpha"),
            Portal(from_world="iamap", origin_point="entree_beta", target_world="beta", teleport_point="spawn_beta")
        ]
        , npcs=[
            NPC("safia", nb_points=2, dialog= r'.\doors\safia\DevIA.exe'),
            NPC("gates", nb_points=4, dialog= r'.\doors\gates\MicrosoftAzure.exe')
        ] )
        self.register_map("alpha", portals=[
            Portal(from_world="alpha", origin_point="exit_alpha", target_world="iamap", teleport_point="back_alpha")
        ]
        , npcs=[
            NPC("charles", nb_points=2, dialog= r'.\doors\charles\Python.exe'),
        ])

        self.register_map("beta", portals=[
            Portal(from_world="beta", origin_point="exit_beta", target_world="iamap", teleport_point="back_beta")
         ]
        , npcs=[
            NPC("jeremy", nb_points=2, dialog= r'.\doors\jeremy\BDD.exe'),
        ])

        self.teleport_player("player")
        self.teleport_npcs()


    def check_npc_collisions(self, dialog_box):
        for sprite in self.get_group().sprites():
            if sprite.feet.colliderect(self.player.rect) and type(sprite) is NPC :
                os.startfile(sprite.dialog)

    # def check_pancarte_collisions(self, dialog_box):
    #     for sprite in self.get_group().sprites():
    #         if sprite.feet.colliderect(self.player.rect) and type(sprite) is pancarte :
    #             dialog_box.execute(sprite.dialog)
                


    def check_collisions(self):
        #portails
        for portal in self.get_map().portals:
            if portal.from_world == self.current_map:
                point = self.get_object(portal.origin_point)
                rect = pygame.Rect(point.x, point.y, point.width, point.height)

                if self.player.feet.colliderect(rect):
                    copy_portal = portal
                    self.current_map = portal.target_world
                    self.teleport_player(copy_portal.teleport_point)


        #collisions
        for sprite in self.get_group().sprites():
            if sprite.feet.collidelist(self.get_walls()) > -1:
                sprite.move_back()



    def teleport_player(self, name):
        point = self.get_object(name)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        self.player.save_location()

    def register_map(self, name, portals=[], npcs=[]):

        #charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame(f'.\doors\{name}.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1

        #définir une liste qui va stocker les rectangles de collision
        walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        #dessiner le groupe de calques
        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        group.add(self.player)

        #récupérer tous les npcs pour les ajouter au groupe
        for npc in npcs:
            group.add(npc)

        #enregistrer la nouvelle carte chargée
        self.maps[name] = Map(name, walls, group, tmx_data, portals, npcs)

    def get_map(self) : return self.maps[self.current_map]

    def get_group(self) : return self.get_map().group
 
    def get_walls(self) : return self.get_map().walls

    def get_object(self, name) : return self.get_map().tmx_data.get_object_by_name(name)

    def teleport_npcs(self):
        for map in self.maps:
            map_data = self.maps[map]
            npcs = map_data.npcs

            for npc in npcs:
                npc.load_points(map_data.tmx_data)
                npc.teleport_spawn()

    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)

    def update(self):
        self.get_group().update()
        self.check_collisions()

        for npc in self.get_map().npcs:
            npc.move()