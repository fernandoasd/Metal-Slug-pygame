import json
from config_game import *

class Ranking():
    def __init__(self, x, y, ancho, alto, pantalla: pygame.Surface):
        
        self.pantalla = pantalla
        self.image = pygame.transform.scale(lista_img_sistema[13],(ancho, alto))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.ancho = ancho
        self.alto = alto
        self.contador = 0


        self.fuente = pygame.font.SysFont("Calibri", 30)
        self.fuente_titulo = pygame.font.SysFont("Calibri", 60)


        self.usuario = self.fuente.render("USUARIO:", True, "yellow")
        self.score = self.fuente.render("SCORE:", True, "yellow")
        

    def mostrar_ranking(self, lista_ranking: list):
        self.pantalla.blit(self.image, (self.rect.x, self.rect.y))
        self.ultimo_usuario = [self.rect.x + 60,  self.rect.y + 145]
        self.ultimo_score = [self.rect.x + self.ancho / 2 + 70, self.rect.y + 145]
        titulo = self.fuente_titulo.render("RANKING", True, "yellow")
        titulo_fondo = self.fuente_titulo.render("RANKING", True, "black")

        self.pantalla.blit(titulo_fondo, (self.rect.x + 100 + 5, self.rect.y + 60))
        self.pantalla.blit(titulo, (self.rect.x + 100, self.rect.y + 60))
        self.pantalla.blit(self.usuario, (self.ultimo_usuario[0], self.ultimo_usuario[1] )) 
        self.pantalla.blit(self.score, (self.ultimo_score[0], self.ultimo_score[1] )) 

        for i in range(len(lista_ranking)):
            if i >= 10:
                break
            else:
                usuario_x_f = self.fuente.render(str(lista_ranking[i]["usuario"]), True, "black")
                score_x_f = self.fuente.render(str(lista_ranking[i]["score"]), True, "black")
                usuario_x = self.fuente.render(str(lista_ranking[i]["usuario"]), True, "white")
                score_x = self.fuente.render(str(lista_ranking[i]["score"]), True, "white")
                
                self.ultimo_usuario = [self.ultimo_usuario[0], self.ultimo_usuario[1] + 30]
                self.ultimo_score = [self.ultimo_score[0], self.ultimo_score[1] + 30]

                self.pantalla.blit(usuario_x_f, (self.ultimo_usuario[0] + 3, self.ultimo_usuario[1])) 
                self.pantalla.blit(score_x_f, (self.ultimo_score[0] + 3, self.ultimo_score[1]))
                self.pantalla.blit(usuario_x, (self.ultimo_usuario[0], self.ultimo_usuario[1])) 
                self.pantalla.blit(score_x, (self.ultimo_score[0], self.ultimo_score[1]))
                


