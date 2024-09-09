import pygame
from config_game import *
from item import *

class Trampa(Item):
    def __init__ (self, image: str, sound: str, init_pos: tuple) -> None:
        super().__init__(image, sound, init_pos)
