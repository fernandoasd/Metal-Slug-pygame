import pygame
from config_game import *
from superficies.GameSprite import GameSprite
# from level import Level

class Item (pygame.sprite.Sprite):

    def __init__ (self,
                lista_img_reposo: list,
                lista_img_activado: list,
                sound: str,
                init_pos: tuple,
                level,
                colision_jugador: bool = True)->None:
        
        super().__init__()
        self.level = level
        # self.image.fill(BLUE) 
        self.con_vida = True
        self.lista_img_reposo = lista_img_reposo
        self.lista_img_activado = lista_img_activado
        self.indice_sprite_item = 0
        self.colision_jugador = colision_jugador
        self.ultima_animacion = 0

        rectangulo = lista_img_reposo[0].get_rect()
        self.image = generar_superficie_transparente(rectangulo.width, rectangulo.height)

        self.rect = self.image.get_rect()
        self.rect.x = init_pos[0]
        self.rect.y = init_pos[1]
        self.projectile_sound = pygame.mixer.Sound(sound)
        self.projectile_sound.set_volume(self.level.sound_level)
        self.speed_x = 0
        self.speed_y = 1
        self.velocidad_maxima_y = 7.0
        

        self.item = GameSprite(self.image, self.rect.x, self.rect.y )

    def play_sound(self):
        self.projectile_sound.play()
        # self.update()

    def update(self)->None:
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.gravedad()
        self.detectar_colision_jugador()
        self.actualizar_estado()

    def mover_verticalmente(self, velocidad_y: float):
        if self.speed_y < self.velocidad_maxima_y:
            self.speed_y += velocidad_y

    
    def gravedad(self):
    # detecta colisiones verticales
        block_hit_list = pygame.sprite.spritecollide(self,
                                                    self.level.platform_list,
                                                    False)
        # si hay colisión
        if len(block_hit_list) > 0:
                for block in block_hit_list:
                    # si esta cayendo y toca piso
                    if self.speed_y > 0:
                        self.rect.bottom = block.rect.top
                        self.speed_y = 0
        else:
            self.mover_verticalmente(0.5)

    def actualizar_estado(self):
        self.animar_item()

    def retraso(self, delay):
        animacion_disponible = False
        tiempo_nueva_animacion = pygame.time.get_ticks()
        tiempo_transcurrido_animacion = tiempo_nueva_animacion - self.ultima_animacion
        if tiempo_transcurrido_animacion >= delay:
            animacion_disponible = True
            # print(f"new {tiempo_nueva_animacion} ant {self.ultima_animacion} dif {tiempo_transcurrido_animacion}")
            self.ultima_animacion = tiempo_nueva_animacion
        return animacion_disponible
    
    def animar_item(self)->None:
        if self.con_vida:
            self.animar(self.lista_img_reposo, 100)
        else:
            self.animar(self.lista_img_activado, 100, True)

        # print(f"{self.indice_sprite_item >= length}, {self.indice_sprite_item} , {length}")

    def detectar_colision_jugador(self):
        if self.colision_jugador:
            block_hit_list = pygame.sprite.spritecollide(self,
                                                        self.level.proyectil_jugador,
                                                        False)
                                                        
            # main_player_git = pygame.sprite.spritecollide(self,
            #                                             self.level.main_player_list,
            #                                             False)
            if block_hit_list:
                self.play_sound()
                self.con_vida = False
            
    def animar(self, sprites_item: list, delay: int, animar_y_morir: bool = False)->None:
        length = len(sprites_item)


        if self.indice_sprite_item >= length:
            self.indice_sprite_item = 0
            if animar_y_morir:
                self.kill()
                self.item.kill()

        rectangulo_animacion = sprites_item[self.indice_sprite_item].get_rect()
        desfase = rectangulo_animacion.height - self.rect.height
        self.item.update_sprite(sprites_item[self.indice_sprite_item], self.rect.x, self.rect.y - desfase)
        if self.retraso(delay):
            self.indice_sprite_item += 1
        
    