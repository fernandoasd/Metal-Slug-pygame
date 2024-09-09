import json
from tkinter import font
import unicodedata
import pygame
import sys
from config_game import *

class MenuPrincipal():
    def __init__(self, pantalla: pygame.Surface):
        self.pantalla = pantalla
        self.activo = True
        self.level = None
        self.nombre_personaje = ""
        self.nivel_seleccionado = ""
        self.score = 0

        self.lista_ranking = []
        self.nombre_valido = False
        self.nivel_valido = False
        self.menu_inicio_activo = True

        # self.rectangulo_menu = pygame.Rect(100, 100, 600, 400)
        self.background = lista_img_sistema[12]
        self.image = lista_img_sistema[11]
        # self.image = lista_img_sistema[11]
        self.rect = self.background.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        self.indice_btn_sonido = 1
        self.click_presionado = False
        self.click_disponible = False
        
        
        # self.boton_sonido = pygame.transform.scale(lista_img_icono_sonido[0],(80, 50))
        # self.rectangulo_btn_sonido = self.boton_sonido.get_rect()
        # self.rectangulo_btn_sonido.x = self.rect.x + 30
        # self.rectangulo_btn_sonido.y = self.rect.y + 130

        self.rectangulo_texto = pygame.Rect(200, 50, 250, 50)

        self.fuente = pygame.font.SysFont("Calibri", 30)
        self.text = ""

        self.texto_seleccione_nivel = "Escriba un nombre de personaje (no vacío)"
        self.nombre_ok = False
        
    def update(self, lista_eventos):
        
        if self.activo:
            if self.menu_inicio_activo: #Menu inicio (pide)
                self.pantalla.blit(self.background, (0, 0))
                pygame.draw.rect(self.pantalla, (180, 180, 180), self.rectangulo_texto, 0)
                texto = self.fuente.render(self.text, True, "red")
                texto_seleccione_nivel = self.fuente.render(self.texto_seleccione_nivel, True, "yellow")

                for evento in lista_eventos:
                        if evento.type == pygame.KEYUP:
                            if self.rectangulo_texto.collidepoint(pygame.mouse.get_pos()):
                                caracter = evento.unicode
                                if evento.key == pygame.K_BACKSPACE:
                                    self.text = self.text[:-1]
                                elif len(caracter) == 1 and unicodedata.category(caracter)[0] != 'C':
                                    # print(caracter)
                                    self.text += caracter

                            if evento.key == pygame.K_RETURN:
                                if not self.nombre_valido:
                                    if self.text != "":
                                        print("OK")
                                        self.nombre_valido =  True
                                        self.menu_inicio_activo = False
                                        self.activo = False
                                        print(f"nombre: {self.text}")
                                        self.nombre_personaje = self.text
                                        # self.texto_seleccione_nivel = "Escriba un nivel (1-3)"
                                        self.nombre_ok = True
                                    else:
                                        print("ingrese un nombre valido")
                                        self.texto_seleccione_nivel = "El nombre no puede estar vacío!"
                                # else:

                                    # if self.text != "1" and self.text != "2" and self.text != "3":
                                    #     self.texto_seleccione_nivel = "error, niveles disponibles: 1-3"
                                    # else:
                                    #     self.nivel_valido = True
                                    #     print(f"nivel: {self.text}")
                                    #     self.nivel_seleccionado = self.text
                                    #     self.activo = False

            self.pantalla.blit(texto, (self.rectangulo_texto.x + (self.rectangulo_texto.width - texto.get_width()) // 2, 
                                    self.rectangulo_texto.y + (self.rectangulo_texto.height - texto.get_height()) // 2))
        
            self.pantalla.blit(texto_seleccione_nivel, (150,1))


            

            # self.handler_events()
            # self.actualizar_botones()
            self.hoover_menu()

    def hoover_menu(self):
        if self.rectangulo_texto.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.pantalla, "Orange", self.rectangulo_texto, 2)

    def get_estado(self):
        return self.activo
    
    def set_estado(self, estado: bool):
        if type(estado) == bool:
            self.activo = estado
    
    def get_nombre_personaje(self):
        if self.nombre_valido:
            return self.nombre_personaje
        else:
            return -1
    
    def get_nivel_elegido(self):
        if self.nivel_valido:
            return self.nivel_seleccionado
        else:
            return -1
    
    

    

    

    # def actualizar_botones(self):
        # if self.indice_btn_sonido == 0:
        #     self.level.sound_level = 0
        #     self.level.music_level = 0
        # elif self.indice_btn_sonido == 1:
        #     self.level.sound_level = 0.05
        #     self.level.music_level = 0.05
        # elif self.indice_btn_sonido == 2:
        #     self.level.sound_level = 0.1
        #     self.level.music_level = 0.1
        # elif self.indice_btn_sonido == 3:
        #     self.level.sound_level = 0.5
        #     self.level.music_level = 0.5

        # self.boton_sonido = pygame.transform.scale(lista_img_icono_sonido[self.indice_btn_sonido],(80, 50))



    