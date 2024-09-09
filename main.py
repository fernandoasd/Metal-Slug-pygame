import pygame
import sys
from config_game import *
from level import *
from level_one import *
from level_two import *
from level_three import *

from Player import *
from projectile import *
from mode import *
from item import *
from ShieldEnemy import *
from menu_inicio import MenuInicio
from menu_principal import MenuPrincipal
from menu import Menu


class main():
    def __init__(self):
        pygame.init()
################### INICIALIZACION ####################################
        # Esta en config.game:
        

        # self.temporizador = pygame.time.set_timer(self.timer_2seg, 2000)
        # if evento.type == self.timer_2seg:
            #     print("2 seg")
            #     for enemigo in self.enemy_list:
            #         enemigo.disparar_jugador()
        # SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)d
        # pantalla = pygame.display.set_mode(SCREEN_SIZE)

        pygame.display.set_caption("Metal-Slug")
        icono = pygame.image.load("./images/rossi_icon.png")
        pygame.display.set_icon(icono)

        self.ruta = "./archivos/ranking.json"

        self.sound_level = 0.1
        self.music_level = 0.1

        # self.nivel_uno = LevelOne(pantalla)
        # self.nivel_dos = LevelTwo(pantalla)
        # self.nivel_tres = LevelThree(pantalla)

        self.nivel_actual = None

        self.score_usuario = 0
        
        self.is_running = True
        self.is_playing = False
        self.is_menu_inicio = True
        self.is_menu = True
        self.is_menu_ingame = False
        self.timer = 0
        self.bandera_inicio = True
        self.bandera_nuevo_nivel = False
        
        self.prox_timer_1seg = 0
        self.prox_timer_4seg = 0
        self.prox_timer_5seg = 0
        
        self.nivel_elegido = 0

        self.menu_principal = MenuPrincipal(pantalla)
        self.menu_ingame = Menu(pantalla)
        self.menu_ingame.level = self

        self.background = pygame.transform.scale(lista_img_sistema[3],(800, 600))
        self.background_rect = self.background.get_rect()
        self.background_rect.x = 0
        self.background_rect.y = 0

        # print_message = pygame.USEREVENT + 0
        # pygame.time.set_timer(print_message, 6000)
        # self.timer_1s = pygame.USEREVENT + 1
        # pygame.time.set_timer(self.timer_1s, 1000)


        # def fps_counter():
        #     font = pygame.font.SysFont("monospace" , 18, bold = True)
        #     fps = str(int(reloj.get_fps()))
        #     fps_t = font.render(f"FPS: {fps}" , 1, pygame.Color("RED"))
        #     pantalla.blit(fps_t,(0,0))

        ################################ IMPRESION DE TEXTO En PANTALLA #################################

        self.reloj = pygame.time.Clock()
        # self.timer_4seg = pygame.USEREVENT + 2
        # pygame.time.set_timer(self.timer_4seg, 4000)
             

        ####################################### BUCLE del JUEGO #################################
        # while is_running:
        #     reloj.tick(FPS)
        while self.is_running:
            self.reloj.tick(FPS)
            # pantalla.blit(self.background, (self.background_rect.x, self.background_rect.y))
            self.event_list = pygame.event.get()
            for evento in self.event_list:
                if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if evento.type == pygame.KEYDOWN:
                     
                    if evento.key == pygame.K_ESCAPE:
                        self.menu_ingame.visible = not self.menu_ingame.visible
                        print("esc")
                    if evento.key == pygame.K_p:
                         print("p")
                         self.is_playing = not self.is_playing
                         print(self.is_playing)
                    # if evento.key == pygame.K_1:
                    #      self.nivel_actual = LevelOne(pantalla)
                    #      print(self.nivel_elegido)
                    # if evento.key == pygame.K_2:
                    #      self.nivel_actual = LevelTwo(pantalla)
                    #      print(self.nivel_elegido)
                    # if evento.key == pygame.K_3:
                    #      self.nivel_actual = LevelThree(pantalla)
                    #      print(self.nivel_elegido)

            if self.is_menu_inicio:
                self.menu_principal.update(self.event_list)
                if not self.menu_principal.get_estado():
                    self.nombre_personaje = self.menu_principal.nombre_personaje
                    self.nivel_elegido = 1
                    print(f"nombre: {self.nombre_personaje} nivel: {self.nivel_elegido}")
                    self.menu_ingame.visible = True
                    self.is_menu_inicio = False
                    self.is_playing = False
                    self.is_menu_ingame = True
                    # self.nivel_elegido = "1"
            # else:
            #     if self.is_menu_ingame:
            #         self.menu_ingame.update(self.event_list)

            if self.menu_ingame.si_eligio_nivel:
                self.nivel_elegido = self.menu_ingame.nivel_eligido
                self.bandera_inicio = True
                self.menu_ingame.si_eligio_nivel = False
                self.menu_ingame.visible = False
                self.bandera_nuevo_nivel = True
            
            # if self.menu_ingame:
                 
            if self.bandera_nuevo_nivel:
                 self.comprobar_nivel_actual()
            
            elif self.is_playing:
                if not self.nivel_actual.dead:
                    self.nivel_actual.update(self.event_list)
                    self.nivel_actual.sound_level = self.sound_level
                    self.nivel_actual.music_level = self.music_level
                    
                    self.score_usuario = self.nivel_actual.jugador.score
                    self.menu_ingame.score = self.score_usuario
                    self.menu_ingame.nombre_personaje = self.nombre_personaje
                    self.nivel_actual.display_partida(self.menu_ingame.score)
                    if self.nivel_actual.enemigos_muertos >= 10:
                        if self.nivel_actual.numero_nivel == "1":
                            self.menu_ingame.nivel_eligido = "2"
                            self.bandera_nuevo_nivel = True
                            self.menu_ingame.si_eligio_nivel = True
                            self.score_usuario = self.nivel_actual.jugador.score
                        elif self.nivel_actual.numero_nivel == "2":
                            self.menu_ingame.nivel_eligido = "3"
                            self.bandera_nuevo_nivel = True
                            self.menu_ingame.si_eligio_nivel = True
                            self.score_usuario = self.nivel_actual.jugador.score
                        else:
                            print("Nivel maximo")
                else:
                    self.menu_ingame.guardar_ranking(self.ruta)
                    self.score_usuario = 0
                    self.timer = 0
                    self.menu_ingame.score = self.score_usuario
                    print("Muerto! score y timer reseteado")
                     


                if not self.is_menu_inicio: 
                    self.timer_1seg()
                    self.timer_4seg()
                    self.timer_10seg()

            self.menu_ingame.update(self.event_list)
            
            pygame.display.flip()

    def comprobar_nivel_actual(self):
            if self.bandera_inicio:
                    if self.nivel_elegido == "1":
                        self.nivel_actual = LevelOne(pantalla)
                        self.nivel_actual.jugador.score = self.score_usuario
                        self.is_playing = True
                        self.bandera_inicio = False
                        self.bandera_nuevo_nivel = False
                        self.is_playing = True
                        print("carga lvl 1")
                    elif self.nivel_elegido == "2":
                        self.nivel_actual = LevelTwo(pantalla)
                        self.nivel_actual.jugador.score = self.score_usuario
                        self.is_playing = True
                        self.bandera_inicio = False
                        self.bandera_nuevo_nivel = False

                        print("carga lvl 2")
                    elif self.nivel_elegido == "3":
                        self.nivel_actual = LevelThree(pantalla)
                        self.nivel_actual.jugador.score = self.score_usuario
                        self.is_playing = True
                        self.bandera_inicio = False
                        self.bandera_nuevo_nivel = False
                        print("carga lvl 3")


    def timer_4seg(self):
        if pygame.time.get_ticks() >= self.prox_timer_4seg:
            self.prox_timer_4seg = pygame.time.get_ticks() + 4000
            print("4 seg, se generan enemigos")
            self.nivel_actual.actualizar_enemigos()
            # print(pygame.time.get_ticks())
    

    def timer_1seg(self):
        if pygame.time.get_ticks() >= self.prox_timer_1seg:
            self.prox_timer_1seg = pygame.time.get_ticks() + 1000
            self.nivel_actual.timer = self.timer
            self.timer += 1
            # print(self.timer)
            # print(pygame.time.get_ticks())
    
    def timer_10seg(self):
        if pygame.time.get_ticks() >= self.prox_timer_5seg:
            self.prox_timer_5seg = pygame.time.get_ticks() + 5000
            self.menu_ingame.guardar_ranking(self.ruta)
            print("guardado automatico de score")
            
    
main()
# print(pygame.time.get_ticks())

        