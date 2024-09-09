import json
from tkinter import font
import unicodedata
import pygame
import sys
from config_game import *
from ranking import Ranking


class Menu():
    def __init__(self, pantalla: pygame.Surface, visible: bool = False):
        self.visible = visible
        self.pantalla = pantalla
        self.score = 0
        self.nombre_personaje = ""
        self.ruta = "./archivos/ranking.json"
        self.level = None
        self.lista_ranking = []
        self.nivel_eligido = 1
        self.si_eligio_nivel = False

        self.fuente = pygame.font.SysFont("Calibri", 30)

        # self.rectangulo_menu = pygame.Rect(100, 100, 600, 400)
        self.image = pygame.transform.scale(lista_img_sistema[13],(400, 500))
        # self.image = lista_img_sistema[11]
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 100

        self.indice_btn_sonido = 1
        self.click_presionado = False
        self.click_disponible = False
        
        self.boton_sonido = pygame.transform.scale(lista_img_icono_sonido[0],(80, 50))
        self.rectangulo_btn_sonido = self.boton_sonido.get_rect()
        self.rectangulo_btn_sonido.x = self.rect.x + 30
        self.rectangulo_btn_sonido.y = self.rect.y + 150

        self.button_lvl_1 = pygame.Rect(50, 400, 80, 80)
        self.button_lvl_2 = pygame.Rect(150, 400, 80, 80)
        self.button_lvl_3 = pygame.Rect(250, 400, 80, 80)

        self.fuente_niveles = self.fuente.render("NIVELES", True, "yellow")
        self.fuente_lvl_1 = self.fuente.render("LVL 1", True, "black")
        self.fuente_lvl_2 = self.fuente.render("LVL 2", True, "black")
        self.fuente_lvl_3 = self.fuente.render("LVL 3", True, "black")

        
        self.fuente_titulo = pygame.font.SysFont("Calibri", 60)
        self.titulo = self.fuente_titulo.render("OPCIONES", True, "yellow")
        self.titulo_fondo = self.fuente_titulo.render("OPCIONES", True, "black")

        # self.rectangulo_texto = pygame.Rect(self.rect.x + 140, self.rect.y + 130, 250, 50)

        self.text = ""

        self.ranking = Ranking(400, 100, 400, 500, self.pantalla)

    def update(self, lista_eventos, activar: bool = False):
        if activar == True:
            self.visible = True
        if self.visible:
            # self.lista_ranking = [{"Usuario1": 320}, {"Usuario2": 250}, {f"{self.nombre_personaje}": f"{self.score}"} ]
            # pygame.draw.rect(self.pantalla, "green", self.rect, 0)
            self.pantalla.blit(self.image, (self.rect.x, self.rect.y))
            self.pantalla.blit(self.boton_sonido, self.rectangulo_btn_sonido)

            pygame.draw.rect(self.pantalla, WHITE, (50, 400, 80, 80))
            pygame.draw.rect(self.pantalla, WHITE, (150, 400, 80, 80))
            pygame.draw.rect(self.pantalla, WHITE, (250, 400, 80, 80))

            # pygame.draw.circle(self.pantalla, (255, 0, 0), pygame.mouse.get_pos(), 30, 2)
            # pygame.draw.rect(self.pantalla, (180, 180, 180), self.rectangulo_texto, 0)
            # texto = self.fuente.render(self.text, True, "red")
            # self.pantalla.blit(texto, (self.rectangulo_texto.x + (self.rectangulo_texto.width - texto.get_width()) // 2, 
                                    #    self.rectangulo_texto.y + (self.rectangulo_texto.height - texto.get_height()) // 2))
            # pygame.draw.rect(self.image, "green", self.boton_sonido, 2)

            for evento in lista_eventos:
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.rectangulo_btn_sonido.collidepoint(pygame.mouse.get_pos()):
                        self.indice_btn_sonido += 1
                        if self.indice_btn_sonido > len(lista_img_icono_sonido) - 1:
                            self.indice_btn_sonido = 0
                    if self.button_lvl_1.collidepoint(pygame.mouse.get_pos()):
                        self.nivel_eligido = "1"
                        self.si_eligio_nivel = True
                    if self.button_lvl_2.collidepoint(pygame.mouse.get_pos()):
                        self.nivel_eligido = "2"
                        self.si_eligio_nivel = True
                    if self.button_lvl_3.collidepoint(pygame.mouse.get_pos()):
                        self.nivel_eligido = "3"
                        self.si_eligio_nivel = True
                    
                # elif self.rectangulo_texto.collidepoint(pygame.mouse.get_pos()) and evento.type == pygame.KEYUP:
                #     caracter = evento.unicode
                #     if evento.key == pygame.K_BACKSPACE:
                #         self.text = self.text[:-1]
                #     elif len(caracter) == 1 and unicodedata.category(caracter)[0] != 'C':
                #         print(caracter)
                #         self.text += caracter
            # self.handler_events()
            self.actualizar_botones()
            self.hoover_menu()
            self.guardar_ranking(self.ruta)
            self.ranking.mostrar_ranking(self.lista_ranking)
            self.pantalla.blit(self.titulo_fondo, (self.rect.x + 100 + 5, self.rect.y + 60))
            self.pantalla.blit(self.titulo, (self.rect.x + 100, self.rect.y + 60))
            self.pantalla.blit(self.fuente_niveles, (self.rect.x + 180, self.rect.y + 220))
            self.pantalla.blit(self.fuente_lvl_1, (60, 430))
            self.pantalla.blit(self.fuente_lvl_2, (160, 430))
            self.pantalla.blit(self.fuente_lvl_3, (260, 430))
            
            

    def actualizar_botones(self):
        if self.indice_btn_sonido == 0:
            self.level.sound_level = 0
            self.level.music_level = 0
        elif self.indice_btn_sonido == 1:
            self.level.sound_level = 0.05
            self.level.music_level = 0.05
        elif self.indice_btn_sonido == 2:
            self.level.sound_level = 0.1
            self.level.music_level = 0.1
        elif self.indice_btn_sonido == 3:
            self.level.sound_level = 0.5
            self.level.music_level = 0.5

        self.boton_sonido = pygame.transform.scale(lista_img_icono_sonido[self.indice_btn_sonido],(80, 50))



    def hoover_menu(self):
        if self.rectangulo_btn_sonido.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.pantalla, "Orange", self.rectangulo_btn_sonido, 2)
        if self.button_lvl_1.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.pantalla, "Orange", self.button_lvl_1, 2)
        if self.button_lvl_2.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.pantalla, "Orange", self.button_lvl_2, 2)
        if self.button_lvl_3.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.pantalla, "Orange", self.button_lvl_3, 2)
        # if self.rectangulo_texto.collidepoint(pygame.mouse.get_pos()):
        #     pygame.draw.rect(self.pantalla, "Orange", self.rectangulo_texto, 2)

            #    if self.click_disponible:
            #         self.btn_sonido = not self.btn_sonido
                    # print("click menu")
                    # print(self.btn_sonido)
                    
    def guardar_json (self, ruta: str, lista_insumos : list)->None:
        with open(ruta, 'w') as file:
            separadores = [","," : "]
            json.dump(lista_insumos, file, indent = 2, separators= separadores)
        # print("se guardo el ranking")


    def cargar_json(self, ruta:str)->None:
        lista = []
        try: 
            with open(ruta, "r") as file:
                lista = json.load(file)
            return lista
        except:
            return -1
        
    def validar_lista(self, lista: list)->bool:
        """si la lista contiene datos devuelve True, caso contrario, False

        Args:
            lista (list): lista a comprobar

        Returns:
            bool: True o False
        """
        lista_cargada = False

        if lista == -1:
            return lista_cargada
        if (len(lista) > 0):
            lista_cargada = True
        return lista_cargada

    def ordenar_lista (self, lista: list, key_uno: str, ascendente_key_uno: bool, key_dos: str, ascendente_key_dos: bool)->None:
        """ordena lista por key_uno, si esta se repite, ordena por key_dos

        Args:
            lista (list): de dict a ordenar
            key_uno (str): primer key
            ascendente_key_uno (bool): orden primer key: True ascendente, False desc
            key_dos (str): segunda key
            ascendente_key_dos (bool): orden primer key: True ascendente, False desc
        """
        if self.validar_lista(lista):
            rango = len(lista)
            swap_flag = True
            while swap_flag:
                swap_flag = False
                for i in range(0, rango -1):
                    j = (i + 1)        
                    if (ascendente_key_uno and (lista[j][key_uno] > lista[i][key_uno])) or (not ascendente_key_uno and (lista[j][key_uno] < lista[i][key_uno])):
                            aux = lista[j]
                            lista[j] = lista[i]
                            lista[i] = aux
                            swap_flag = True
                    elif (lista[j][key_uno] == lista[i][key_uno]):
                        if (ascendente_key_dos and (lista[j][key_dos] > lista[i][key_dos])) or (not ascendente_key_dos and (lista[j][key_dos] < lista[i][key_dos])):
                            aux = lista[j]
                            lista[j] = lista[i]
                            lista[i] = aux
        else:
            print("error, lista vacía")
            return -1

    def guardar_ranking(self, ruta: str):
        existe_usuario = False
        self.lista_ranking = self.cargar_json(ruta)
        if self.lista_ranking == -1:
            # print("no se encontro .json, se crea uno")
            lista = []
            diccionario = {}
            diccionario["usuario"] = self.nombre_personaje
            diccionario["score"] = self.score
            lista.append(diccionario)
            self.guardar_json(ruta, lista)
        else:
            # print("json encontrado")
            for ranking in self.lista_ranking:
                    if ranking["usuario"] == self.nombre_personaje:
                        # print("se encontro usuario")
                        if self.score >= ranking["score"]:
                            print("rankign actual es mayor, score actuliazado!")
                            ranking["score"] = self.score
                            existe_usuario = True
            
            if existe_usuario:
                self.ordenar_lista(self.lista_ranking, "score", True, "usuario", True)
                self.guardar_json(ruta, self.lista_ranking)
            else:
                diccionario = {}
                diccionario["usuario"] = self.nombre_personaje
                diccionario["score"] = self.score
                self.lista_ranking.append(diccionario)
                self.ordenar_lista(self.lista_ranking, "score", True, "usuario", True)
                self.guardar_json(ruta, self.lista_ranking)

