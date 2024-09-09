import pygame
from config_game import *
from item import *

class Recompensa(Item):
    def __init__ (self, imagen_inactivo: list, imagen_activo: list, sound: str, init_pos: tuple) -> None:
        super().__init__(imagen_inactivo, imagen_activo, sound, init_pos)