import pygame
from config_game import *
from item import *

class Projectile (Item):

    shot_direction = [1, 0]

    def __init__ (self,
                img_reposo: list,
                img_activado: list,
                sound: str,
                init_pos: tuple,
                shot_direction: list,
                level) -> None:
        
        super().__init__(img_reposo, img_activado, sound, init_pos, level, False)
        self.projectile_speed = PROJECTILE_SPEED
        self.shot_direction = shot_direction
        self.image = pygame.transform.scale(img_reposo[0], PROJECTILE_SIZE)
        self.level = level
        
    def update(self)->None:
        self.rect.x += self.projectile_speed * self.shot_direction[0]
        self.rect.y += self.projectile_speed * self.shot_direction[1]
        self.detectar_colision_plataformas()
        self.actualizar_estado()

    def detectar_colision_plataformas(self):
        block_hit_list = pygame.sprite.spritecollide(self,
                                                    self.level.platform_list,
                                                    False)

        if len(block_hit_list) > 0 or self.rect.x > SCREEN_WIDTH or self.rect.y < 0:
            self.projectile_speed = 0
            self.con_vida = False

    
            
        
    

        











