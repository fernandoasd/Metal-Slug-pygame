import pygame
from config_game import *
from superficies.GameSprite import *
from projectile import Projectile

class Player(pygame.sprite.Sprite):
    """ This class represent the player """   
    
    def __init__(self, player_start_pos : tuple):
        """ constructor of the player"""
        super().__init__()
        self.level = None
        self.lives = 3
        
        self.ultima_colision_enemigo = 0
        # self.colision = False
        
        self.indice_sprite_torso = 0
        self.indice_sprite_pierna = 0
        self.doble_salto = False

        self.salta = False
        self.va_derecha = False
        self.va_izquierda = False
        self.estado_anterior_derecho = True
        
        self.image= pygame.Surface((PLAYER_SIZE[0], PLAYER_SIZE[1] + PLAYER_SIZE[3]))
        self.image.fill(RED)
        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect()

        self.__visible = True

        self.rect.x = player_start_pos[0]
        self.rect.y = player_start_pos[1]
        
        self.pm_versor = [1, 0]

        self.speed_x = 0
        self.speed_y = 0
        self.walls = None

        @property
        def visible(self):
            return self.__visible
        
        @visible.setter
        def visible(self, visible : str):
            self.__visible = visible

    def change_visibility(self):
        self.__visible = not self.__visible
        self.change_set_colorkey()

    def change_set_colorkey(self):
        if self.__visible:
            self.image.set_colorkey(None)
        else:
            self.image.set_colorkey(RED)

    def update(self):
        """desplazamiento del personaje"""


        # left/right movement
        self.rect.x += self.speed_x

        # make sure it doesn't go off the screen
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        
        if self.rect.left < 0:
            self.rect.left = 0

        # detecta colisiones al moverse horizontalmente
        block_hit_list = pygame.sprite.spritecollide(self,
                                                    self.level.platform_list,
                                                    False)
        
        for block in block_hit_list:
            if self.speed_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        # up/down movement
        self.rect.y += self.speed_y

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
                        self.salta = False
                        self.doble_salto = True

                    else:
                        # Si le pega un cabezazo a un bloque rebota hacia abajo
                        self.rect.top = block.rect.bottom
                        self.move_down() 
        else:
            self.calculate_gravity()
            self.salta = True



    def move_right(self):
        self.speed_x = 7
        self.va_derecha = True
        self.va_izquierda = False
        # self.update()

    def move_left(self):
        self.speed_x = -7
        self.va_izquierda = True
        self.va_derecha = False
        # self.update()

    def move_up(self):
        self.speed_y = -25
        self.salta = True
    
    def move_down(self):
        self.speed_y = 5

    def stop(self):
        self.speed_x = 0
        self.indice_sprite_torso = 0
        self.va_derecha = False
        self.va_izquierda = False
    
    def start_position(self, pos : tuple):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def calculate_gravity(self):
        """Calculate the effect of gravity"""

        self.speed_y += 2.8

        # check if it is on the borders of the screen
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.speed_y > 0:
            self.speed_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump (self):
        """ called when the user press the JUMP button"""

        self.rect.y += 2
        plataform_hit_list = pygame.sprite.spritecollide(self,
                                                        self.level.platform_list,
                                                        False)
        self.rect.y -= 2

        if len(plataform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.move_up()
        elif self.doble_salto:
            self.move_up()
            self.doble_salto = False


         
    def point_direction(self):
        mouse_position = pygame.mouse.get_pos()
        direccion = [mouse_position[0] - self.rect.x,
                     mouse_position[1] - self.rect.y]

        modulo = direccion[0]**2 + direccion[1]**2
        modulo = modulo**0.5
        # vector unitario de posicion personaje-posicion mouse
        self.pm_versor = [direccion[0] * PROJECTILE_SPEED // modulo, direccion[1] * PROJECTILE_SPEED // modulo]
        # print(f"{self.pm_versor[0]} , {self.pm_versor[1]}")

    def detectar_colision_enemigo(self, delay):
        block_hit_list = pygame.sprite.spritecollide(self,
                                                    self.level.enemy_list,
                                                    False)
    
        if block_hit_list:
                if self.retraso(delay):
                    self.jump()
                    self.lives += -1
                    print(print(f"Impacto con enemigo. vidas Rossi -1: {self.lives}"))

    def detectar_colision_trampa(self, delay):
        block_hit_list = pygame.sprite.spritecollide(self,
                                                    self.level.trap_list,
                                                    False)
    
        if block_hit_list:
            if self.retraso(delay):
                self.jump()
                self.lives += -1
                block_hit_list[0].play_sound()
                block_hit_list[0].con_vida = False
                print(print(f"Impacto trampa. vidas Rossi -1: {self.lives}"))

    def detectar_colision_recompensa(self, delay):
        block_hit_list = pygame.sprite.spritecollide(self,
                                                    self.level.rewards_list,
                                                    False)
    
        if block_hit_list:
            if self.retraso(delay):
                self.lives += 1
                block_hit_list[0].play_sound()
                block_hit_list[0].con_vida = False
                print(print(f"reward. vidas Rossi +1: {self.lives}"))

    def retraso(self, delay):
        disponible = False
        tiempo_nuevo = pygame.time.get_ticks()
        tiempo_transcurrido = tiempo_nuevo - self.ultima_colision_enemigo
        if tiempo_transcurrido >= delay:
            disponible = True
            # print(f"new {tiempo_nuevo} ant {self.ultima_colision_enemigo} dif {tiempo_transcurrido}")
            self.ultima_colision_enemigo = tiempo_nuevo
        return disponible












