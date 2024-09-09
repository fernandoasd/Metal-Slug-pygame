from level import *
from config_game import *
from superficies.GameSprite import *
from ShieldEnemy import ShieldEnemy
from recompensa import Recompensa
from menu import Menu

class LevelTwo(Level):
    def __init__(self, pantalla: pygame.Surface):
        ######################################### INICIALIZACION ####################################
        # configuracion inicial
        # pantalla = pygame.display.set_mode(SCREEN_SIZE)
        w = pantalla.get_width()
        h = pantalla.get_height()

        self.sound_level = 0.1
        self.music_level = 0.1

        self.cantidad_respawn = 3

        # background:
        background =  backgrounds[3]
        # musica
        pygame.mixer.init()
        # sonido_fondo = pygame.mixer.Sound("./music/02. The Military System.mp3")
        # sonido_fondo.set_volume(self.music_level)
        # sonido_fondo.play()

        ########### GENERO UN EVENTO PROPIO CADA 100 ms #################################
        tick = pygame.USEREVENT + 0
        pygame.time.set_timer(tick, 100)

        ##################### PERSONAJE Y SPRITES GROUPS #################################
        personaje_principal = MainPlayer((150, 350))
        enemigo = ShieldEnemy((600, 400))
        trampa = Item(lista_img_trampa_reposo, lista_img_trampa_activada, SHOT_SOUND, (370, 1), self)
        recompensa = Item(img_item_vida, img_item_vida, SHOT_SOUND, (500, 1), self)

        enemigo.speed_x = 2
        enemy_list = []
        trap_list = []
        reward_list = []
        active_sprites_list = pygame.sprite.Group()
        personaje_principal.level = self
        enemigo.level = self
        trampa.level = self
        recompensa.level = self

        # menu =  Menu(pantalla)
        # menu.level = self

        active_sprites_list.add(personaje_principal)
        active_sprites_list.add(personaje_principal.legs)
        active_sprites_list.add(personaje_principal.torso)
        active_sprites_list.add(enemigo)
        active_sprites_list.add(enemigo.torso)
        active_sprites_list.add(trampa)
        active_sprites_list.add(trampa.item)
        active_sprites_list.add(recompensa)
        active_sprites_list.add(recompensa.item)
        enemy_list.append(enemigo)
        trap_list.append(trampa)
        reward_list.append(recompensa)

        
        ################################ IMPRESION DE TEXTO En PANTALLA #################################
        
        super().__init__(pantalla, personaje_principal, active_sprites_list, background)

        self.enemy_list = enemy_list
        self.trap_list = trap_list
        self.rewards_list = reward_list
        self.numero_nivel = "2"

        pygame.mixer.init()
        sonido_fondo = pygame.mixer.Sound("./music/02. The Military System.mp3")
        sonido_fondo.set_volume(self.music_level)
        sonido_fondo.play()
        #################### CREACION DE PLATAFORMAS DE NIVEL #########################################################################

        self.create_platforms()

    def create_platforms(self):
        ######################################### PLATAFORMAS #################################
        plataforms = [
            # x, y, image (0-8)
            [200, 330, 0], 
            [100, 440, 1],
            [550, 250, 1],
            [750, 200, 1],
            [50, 550, 2],
            # [730, 520, 3],
            [0, 550, 0],
            [130, 550, 0],
            [230, 550, 0],
            [330, 550, 1],
            [430, 550, 0],
            [530, 550, 1],
            [630, 550, 0],
            [730, 550, 0],
            # [750, 250, 5],
            # [250, 300, 6],
            # [500, 400, 7],
            [320, 370, 1],
            # [380, 340, 7],
            # [540, 320, 7],
            # [1, 500, 7],
            # [250, 700, 8]
        ]

        piso = pygame.Surface((SCREEN_WIDTH + 4, 10))
        sprite_piso = GameSprite(piso, -2, SCREEN_HEIGHT - 8)
        self.platform_list.add(sprite_piso)

        for platform in plataforms:
            sprite_platform = GameSprite(platforms_level_2[platform[2]], platform[0] , platform[1])
            self.platform_list.add(sprite_platform)

    def actualizar_enemigos(self):
        for x in range(self.cantidad_respawn):
            if len(self.enemy_list) <= self.cantidad_enemigos_max:
                pos_x_random = random.randint(2, 700)
                pos_y_random = random.randint(2, 100)
                self.enemigo2 = ShieldEnemy((pos_x_random, pos_y_random))
                self.enemigo2.level = self
                self.active_sprites_list.add(self.enemigo2)
                self.active_sprites_list.add(self.enemigo2.torso)
                self.enemy_list.append(self.enemigo2)
                print(f"se generan enemigos {x}")