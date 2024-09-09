from Player import *


class MainPlayer(Player):
    def __init__(self, player_start_pos : tuple):

        
        Player.__init__(self, player_start_pos)

        self.score = 0

        self.legs = GameSprite(piernas_rossi_derecha[0], self.rect.x, self.rect.y + PLAYER_SIZE[3] + 10)
        self.torso = GameSprite(torso_rossi_derecha[0], self.rect.x, self.rect.y)

        self.CENTER = (self.rect.x + (self.rect.width // 2), self.rect.y + (self.rect.height // 2)) 

    def animar_piernas(self, sprites_piernas: list, izquierda: bool = False)->None:
        self.desfase = 0
        if izquierda:
            self.desfase = 10* multiplicador_tamanio
        length = len(sprites_piernas)
        if self.indice_sprite_pierna >= length:
            self.indice_sprite_pierna = 0

        self.legs.update_sprite(sprites_piernas[self.indice_sprite_pierna], self.rect.x + self.desfase, self.rect.y + PLAYER_SIZE[3] + 10 * multiplicador_tamanio)
        self.indice_sprite_pierna += 1

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
                self.animar_piernas(piernas_rossi_derecha)
                self.animar_torso(torso_rossi_derecha)
                self.estado_anterior_derecho = True
            else:
                if self.va_izquierda:
                    self.animar_piernas(piernas_rossi_izquierda, 1)
                    self.animar_torso(torso_rossi_izquierda, 1)
                    self.estado_anterior_derecho = False
                else:
                    if self.estado_anterior_derecho:
                        self.animar_piernas(rossi_idle_legs_derecha)
                        self.animar_torso(rossi_torso_idle_derecha)
                    else:
                        self.animar_piernas(rossi_idle_legs_izquierda, 1)
                        self.animar_torso(rossi_torso_idle_izquierda, 1)
        else:
            if self.va_izquierda or not self.estado_anterior_derecho:
                self.animar_piernas(lista_imagenes_transparentes)
                self.animar_torso(rossi_saltando_izquierda, 1)
                self.estado_anterior_derecho = False
            else:
                if self.va_derecha or self.estado_anterior_derecho:
                    self.animar_piernas(lista_imagenes_transparentes)
                    self.animar_torso(rossi_saltando_derecha)
                    self.estado_anterior_derecho = True
    
    