from config_game import *
import random
from Player import *

class ShieldEnemy(Player):
    def __init__(self, player_start_pos : tuple):
        self.bandera_primera_caida = False
        Player.__init__(self, player_start_pos)

        self.lives = 2

        self.con_vida = True
        self.torso = GameSprite(shield_enemy_derecha[0], self.rect.x, self.rect.y)
        self.CENTER = (self.rect.x + (self.rect.width // 2), self.rect.y + (self.rect.height // 2)) 

    def animar_torso(self, sprites_torso: list, izquierda: bool = False)->None:
        self.desfase = 0
        if izquierda:
            self.desfase = 0
        length = len(sprites_torso)
        if self.indice_sprite_torso >= length:
            self.indice_sprite_torso = 0

        self.torso.update_sprite(sprites_torso[self.indice_sprite_torso], self.rect.x - self.desfase, self.rect.y + 3 * multiplicador_tamanio)
        self.indice_sprite_torso += 1

    def actualizar_estado(self)->None:
        if not self.salta:
            if self.va_derecha:
                # self.animar_piernas(piernas_rossi_derecha)
                self.animar_torso(shield_enemy_derecha)
                self.estado_anterior_derecho = True
            else:
                if self.va_izquierda:
                    # self.animar_piernas(piernas_rossi_izquierda, 1)
                    self.animar_torso(shield_enemy_izquierda, 1)
                    self.estado_anterior_derecho = False
                else:
                    if self.estado_anterior_derecho:
                        # self.animar_piernas(rossi_idle_legs_derecha)
                        self.animar_torso(shield_enemy_derecha)
                    else:
                        # self.animar_piernas(rossi_idle_legs_izquierda, 1)
                        self.animar_torso(shield_enemy_izquierda, 1)
        else:
            if self.va_izquierda or not self.estado_anterior_derecho:
                # self.animar_piernas(lista_imagenes_transparentes)
                self.animar_torso(shield_enemy_izquierda, 1)
                self.estado_anterior_derecho = False
            else:
                if self.va_derecha or self.estado_anterior_derecho:
                    # self.animar_piernas(lista_imagenes_transparentes)
                    self.animar_torso(shield_enemy_derecha)
                    self.estado_anterior_derecho = True

    def movimiento_random(self):
        """al instanciarse hay igual posibilidad de moverse derecha / izquierda 
            si bandera = False se activa una vez
        """
        if not self.bandera_primera_caida:
            radom_int = random.randint(0,1)
            if radom_int:
                self.move_right()
                # print("random: der")
            else:
                self.move_left()
                # print("random: izq")
            self.bandera_primera_caida = True

    def invertir_sentido(self):
        """una vez que cae ya puede empezar a moverse

        Args:
            moverse_derecha (bool): true - move_right, false - move left
            bandera_primera_caida (_type_): True: ejecuta accion
        """
        if self.bandera_primera_caida:
            if self.va_derecha:
                self.move_left()
            else:
                self.move_right()
            # print("enemigo invierte sentido")

    # def invertir_movimiento(self):
    #     self.moverse_derecha = not self.moverse_derecha

    def update(self):
        # self.movimiento_automatico()

        if self.lives <= 0:
            self.level.jugador.score += 100
            self.con_vida = False
            self.kill()
            self.torso.kill()
        """desplazamiento del personaje"""
        # left/right movement
        self.rect.x += self.speed_x

        # make sure it doesn't go off the screen
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.invertir_sentido()
        
        if self.rect.left < 0:
            self.rect.left = 0
            self.invertir_sentido()

        # detecta colisiones al moverse horizontalmente
        block_hit_list = pygame.sprite.spritecollide(self,
                                                    self.level.platform_list,
                                                    False)
        
        if len(block_hit_list) > 0:
            
            for block in block_hit_list:
                if self.speed_x > 0:
                    self.rect.right = block.rect.left
                else:
                    self.rect.left = block.rect.right
            self.invertir_sentido()
        # up/down movement
        self.rect.y += self.speed_y

        # detecta colisiones verticales
        block_hit_list = pygame.sprite.spritecollide(self,
                                                    self.level.platform_list,
                                                    False)
        # si hay colisión
        if len(block_hit_list) > 0:
                
                self.movimiento_random()

                for block in block_hit_list:
                    # si esta cayendo y toca piso
                    if self.speed_y > 0:
                        self.rect.bottom = block.rect.top
                        self.salta = False

                    else:
                        # Si le pega un cabezazo a un bloque rebota hacia abajo
                        self.rect.top = block.rect.bottom
                        self.move_down() 
        else:
            self.calculate_gravity()
            self.salta = True

        self.detectar_colision_proyectil(500)

    def detectar_colision_proyectil(self, delay):

        block_hit_list = pygame.sprite.spritecollide(self,
                                                    self.level.proyectil_jugador,
                                                    False)

        if block_hit_list:
            if self.retraso(delay):
                self.lives += - 1
                block_hit_list[0].projectile_speed = 0
                block_hit_list[0].con_vida = False
                # print(f"vidas npc: {self.lives}")
        

        
        
            
