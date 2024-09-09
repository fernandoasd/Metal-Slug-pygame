import pygame
import sys
from config_game import *
from Player import *
from projectile import *
from mode import *
# from item import *
from superficies.GameSprite import *
from MainPlayer import *
from ShieldEnemy import *
from trampa import *


class Level:
    def __init__(self, pantalla: pygame.Surface,
                personaje_principal: MainPlayer,
                active_sprites_list: pygame.sprite.Group,
                background: pygame.Surface):
    
        self.pantalla = pantalla
        self.w = pantalla.get_width()
        self.h = pantalla.get_height()
        self.jugador = personaje_principal
        self.active_sprites_list = active_sprites_list
        self.background =  background
        self.event_list = None
        self.nombre_personaje = ""
        self.score = 0
        self.cantidad_enemigos_max = 5
        self.timer = 0
        self.enemigos_muertos = 0
        self.numero_nivel = 0

        self.font = pygame.font.SysFont("monospace" , 50, bold = True)
        self.font_timer = pygame.font.SysFont("monospace" , 40, bold = True)
        self.font_timer_border = pygame.font.SysFont("monospace" , 40, bold = True)
        


        ######################### SONIDOS DEL JEUGO ################
        self.sound_level = 0.1
        self.music_level = 0.1

        self.is_playing = False
        self.is_running = True
        self.dead = False
        self.timer = 0

        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.trap_list = pygame.sprite.Group()
        self.rewards_list = pygame.sprite.Group()
        self.main_player_list = pygame.sprite.Group()
        self.proyectil_jugador = pygame.sprite.Group()
        self.proyectil_npc = pygame.sprite.Group()


        self.main_player_list.add(self.jugador)

        ######## comprobar utilizacion variables:
        self.actual_level = self
        ####### START CLOCK #######
        

    # def play(self, event_list):
    #     self.is_playing = True

        
        
        
    #     self.update()
    #     # FPS #
    #     # fps_counter()
    #     # pygame.display.update()


    def update(self, event_list):
        self.score = self.jugador.score
        self.jugador.detectar_colision_enemigo(700)
        self.jugador.detectar_colision_trampa(700)
        self.jugador.detectar_colision_recompensa(700)
        self.actualizar_pantalla()
        self.draw_rectangles()
        self.game_over()
        self.handler_events(event_list)
        # self.display_partida()
        self.blitear_timer(self.timer, 650, 5)
        
    def handler_events(self, event_list):

        ####################### TECLAS JUGADOR ###########################
        for evento in event_list:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_a:
                    self.jugador.move_left()
                if evento.key == pygame.K_d:
                    self.jugador.move_right()
                if evento.key == pygame.K_w:
                    self.jugador.jump()
                if evento.key == pygame.K_SPACE:
                    self.jugador.jump()
                if evento.key == pygame.K_TAB:
                    print("tab")
                    change_mode()
                # if evento.key == pygame.K_ESCAPE:
                    # self.menu.visible = not self.menu.visible

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_a and self.jugador.speed_x < 0:
                    self.jugador.stop()
                    # print("A UP - STOP")
                if evento.key == pygame.K_d and self.jugador.speed_x > 0:
                    self.jugador.stop()
                    # print("D UP - STOP")
                if evento.key == pygame.K_w and self.jugador.speed_y < 0:
                    pass 
                    # print("W UP - STOP")

                        ########## EVENTO MOUSE (apuntar y disparar) #########################

            if evento.type == pygame.MOUSEBUTTONDOWN:

               # [0] - left click
               # [1] - middle click
               # [2] - right click
            #    if pygame.mouse.get_pressed()[0]:
            #       self.disparar_proyectil()
                if evento.button == 1:
                    self.disparar_proyectil()
                    # print("click 1", evento.pos) # Objeto evento
                # if evento.button == 2:
                #     # print("click 2", evento.pos)
                # if evento.button == 3:
                #     # print("click 3", evento.pos)
                # if evento.button == 4:
                #     # print("Scroll Up", evento.pos)
                # if evento.button == 5:
                #     # print("Scroll Down", evento.pos)


            # ################################ EVENTOS PROPIOS #########################
            # if evento.type == pygame.USEREVENT:
            #     if evento.type == tick:
            #         # aca cuelgo mis eventos bw
            #         pass

    def blitear_timer(self, contador: any, x, y):
        self.imprimir_texto(f"{contador} seg", x, y)
        self.timer = contador
        # timer_border = self.font_timer_border.render(str(contador), True, (0, 0, 0))
        # timer_filler = self.font_timer.render(str(contador), True, (255, 255, 255))
        # pantalla.blit(timer_border, (x + 3, y))
        # pantalla.blit(timer_filler, (x, y))

        

    def disparar_proyectil(self):
        self.jugador.point_direction()
        disparo = Projectile(lista_img_proyectil,
                            lista_img_explosion_1,
                            SHOT_SOUND,
                            (self.jugador.rect.x, self.jugador.rect.y),
                            self.jugador.pm_versor, self)
        disparo.level = self
        self.active_sprites_list.add(disparo)
        self.active_sprites_list.add(disparo.item)
        self.proyectil_jugador.add(disparo)
        self.proyectil_jugador.add(disparo.item)
        disparo.play_sound()
        # print("corchazo")


    # def active_debug_mode(self, event_list):
    #      for evento in event_list:
    #         if evento.type == pygame.KEYDOWN:
    #             if evento.key == pygame.K_TAB:
    #                 print("tab")
    #                 change_mode()
    #             if evento.key == pygame.K_ESCAPE:
    #                 self.menu.visible = not self.menu.visible


    ################################ IMPRESION DE TEXTO EN PANTALLA #################################
    
    def imprimir_texto(self, cadena: str, x: int, y: int)->None:
        cadena =  str(cadena)
        cadena_a_imprimir_f = self.font_timer_border.render(cadena, 1, pygame.Color("black"))
        cadena_a_imprimir = self.font_timer.render(cadena, 1, pygame.Color("white"))
        pantalla.blit(cadena_a_imprimir_f, (x + 5, y))
        pantalla.blit(cadena_a_imprimir, (x, y))

    def display_partida(self, jugador_score: int):
        item_vida = pygame.transform.scale(img_item_vida[0].convert_alpha(),(30, 40))
        for x in range (0, self.jugador.lives):
            pantalla.blit(item_vida, (5 + (x * 31), 5))
        
        self.imprimir_texto(str(f"Score: {jugador_score}"), 5, 45)



        # self.imprimir_texto(str(f"Vidas: {self.jugador.lives}"), 0, 90)
        # self.imprimir_texto(str(f"Score: {self.jugador.score}"), 0, 120)

    def draw_rectangles(self):
        # DEBUG MODE #
        if get_mode():
                self.jugador.lives = 5
                pygame.draw.rect(pantalla, GREEN, self.jugador.rect, 2)
                for enemy in self.enemy_list:
                    pygame.draw.rect(pantalla, RED, enemy.rect, 2)
                for plataforma in self.platform_list:
                    pygame.draw.rect(pantalla, VIOLET, plataforma.rect, 2)
                for trampa in self.trap_list:
                    pygame.draw.rect(pantalla, YELLOW, trampa.rect, 2)
                for disparo in self.proyectil_jugador:
                    pygame.draw.rect(pantalla, BLUE, disparo.rect, 2)
                for recompensa in self.rewards_list:
                    pygame.draw.rect(pantalla, "Orange", recompensa.rect, 2)
                # pygame.draw.rect(pantalla, "red", self.menu.rect, 2)
                # self.imprimir_texto(str(f"Speed x: {self.jugador.speed_x:.2f}"), 0, 30)
                # self.imprimir_texto(str(f"Speed y: {self.jugador.speed_y:.2f}"), 0, 60)
                

    def draw(self, screen: pygame.surface.Surface):
        """ Draw all in this level"""

        # draw the background
        screen.fill(BLUE)
        self.background = pygame.transform.scale(self.background, (self.w, self.w))

        # self.background = pygame.transform.scale(self.background, SCREEN_SIZE)
        screen.blit(self.background, (0, 0))

        # Draw all the sprite list of the level
        self.platform_list.draw(screen)
        self.active_sprites_list.draw(pantalla)
    
    ##################################### PANTALLA ###############################
    def actualizar_pantalla(self):
        self.jugador.actualizar_estado()
        
        for enemy in self.enemy_list:
            enemy.actualizar_estado()

        for trap in self.trap_list:
            trap.actualizar_estado()
        
        for reward in self.rewards_list:
            reward.actualizar_estado()

        self.active_sprites_list.update()

        self.actual_level.draw(pantalla)

        for enemy in self.enemy_list:
            if not enemy.con_vida:
                self.enemy_list.remove(enemy)
                print("enemy kill map")
                self.enemigos_muertos += 1
                print(f"enemigos muertos: {self.enemigos_muertos}")


        for trap in self.trap_list:
            if not trap.con_vida:
                self.trap_list.remove(trap)
                print("trap kill map")

        for reward in self.rewards_list:
            if not reward.con_vida:
                self.rewards_list.remove(reward)
                print("reward kill map")

    def game_over(self):
        if self.jugador.lives <= 0 or self.timer > 60000 * 3:
            self.font = pygame.font.SysFont("monospace" , 60, bold = True)
            cadena_a_imprimir = self.font.render("GAME-OVER", 1, pygame.Color("RED"))
            # pantalla.blit(img_game_over, (0, 0))
            pantalla.blit(cadena_a_imprimir, (300, 10))
            self.is_playing = False
            self.dead = True

    def exit(self):
        self.is_running = False

    def show_game_over_screen(self):
        pass
