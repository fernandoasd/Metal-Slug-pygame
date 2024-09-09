import pygame
from pygame.sprite import Group
from config_game import *
from superficies.GameSurface import *
from superficies.GameSprite import *
from Player import Player

class Afwea(object):
    """Generic super_class used to create a level.
        It's needed to create a child class for each specific level.
    """

    def __init__(self, player):
        """ Need the player for when the moving platform colides with the player"""
        # self.platform_list = pygame.sprite.Group()
        # self.enemy_list = pygame.sprite.Group()
        self.player = player

    # def update(self):
    #     """ update all in the level"""
    #     self.platform_list.update()
    #     self.enemy_list.update()
    


class Level01 (Afwea):
    """ class of the level 1"""

    def __init__(self, player):
        """ constructor of the level 1"""
        
        # Call the parent constructor
        Afwea.__init__(self, player)

        # list with x, y , width and height of this level
        level = [
            # x     y   width  height
            [100,  500,  150,  50], 
            [300,  400,  200,  50],
            [550,  300,  200,  50],
        ]

        # objeto1 = nivel_1[0]

        # iterate the array level and add platforms
        # for platform in level:
        #     block_platform = GameSurface(platform[2], platform[3])
        #     block_platform.rect.x = platform[0]
        #     block_platform.rect.y = platform[1]
        #     block_platform.player = self.player
        #     self.platform_list.add(block_platform)

        





    






