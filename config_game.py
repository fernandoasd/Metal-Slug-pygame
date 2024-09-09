
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
pantalla = pygame.display.set_mode(SCREEN_SIZE)

FPS = 25

multiplicador_tamanio = 1
PLAYER_WIDTH = 29
PLAYER_HEIGHT = 46
#             largo_torso    alto_torso   largo_legs  alto_legs
PLAYER_SIZE = (29 * multiplicador_tamanio     , 30  * multiplicador_tamanio   , 21  * multiplicador_tamanio   , 16  * multiplicador_tamanio)


PLAYER_CENTER = (PLAYER_WIDTH // 2, PLAYER_HEIGHT // 2)

player_image = r".\images\3.png"
player_legs = r".\images\idle\8.png"
background_image = r".\images\fondo.png"
PLAYER_START_POS = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
BORDER_WALL_WIDTH = 5
PROJECTILE_SIZE = (10, 10)
SHOT_SOUND = r"./assets\sounds\disparo\st2_0A_shot.wav"
impacto_disparo = r"assets\sounds\disparo\gen_2F_impacto.wav"
PROJECTILE_SPEED = 7
wall_visible_flag = True

# sound_level = 0.1
# music_level = 0.1

WHITE = (255, 255, 255)
BLACK = (32, 33, 36)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (221, 68, 234)
YELLOW = (249, 205, 53)




def girar_imagenes(lista_original, flip_factor_escala: bool, flip_y: bool):
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_factor_escala, flip_y))
    return lista_girada

img_game_over = pygame.transform.scale(pygame.image.load("./assets/images/game_over.png").convert_alpha(),(800, 600))


# assets\images\system_setup\0.png
    

factor_escala = 1.25
lista_img_sistema = [
    pygame.image.load("./assets/images/system_setup/0.png").convert_alpha(),
    pygame.image.load("./assets/images/system_setup/1.png").convert_alpha(),
    pygame.image.load("./assets/images/system_setup/2.png").convert_alpha(),
    pygame.image.load("./assets/images/system_setup/3.png").convert_alpha(),
    pygame.image.load("./assets/images/system_setup/4.png").convert_alpha(),
    pygame.image.load("./assets/images/system_setup/5.png").convert_alpha(),
    pygame.image.load("./assets/images/system_setup/6.png").convert_alpha(),
    pygame.image.load("./assets/images/system_setup/7.png").convert_alpha(),
    pygame.image.load("./assets/images/system_setup/8.png").convert_alpha(),
    pygame.image.load("./assets/images/system_setup/9.png").convert_alpha(),
    pygame.image.load("./assets/images/system_setup/10.png").convert_alpha(),
    pygame.image.load("./assets/images/system_setup/11.png").convert_alpha(),
    pygame.transform.scale(pygame.image.load("./assets/images/system_setup/inicio_metal.jpg").convert_alpha(),(800, 600)),
    pygame.image.load("./assets/images/system_setup/ranking.png").convert_alpha()
    ]

lista_img_proyectil = [
    pygame.transform.scale(pygame.image.load("./assets/images/projectile/0.png").convert_alpha(),(PROJECTILE_SIZE[0], PROJECTILE_SIZE[0]))
    ] 

lista_img_explosion_1 = [
    pygame.transform.scale(pygame.image.load("./assets/images/explosion/1/0.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/explosion/1/1.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/explosion/1/2.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/explosion/1/3.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/explosion/1/4.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
]

rossi_torso_idle_derecha = [
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/idle/torso/0.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/idle/torso/1.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/idle/torso/2.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/idle/torso/3.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/idle/torso/4.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/idle/torso/5.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/idle/torso/6.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/idle/torso/7.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/idle/torso/8.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/idle/torso/9.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/idle/torso/10.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/idle/torso/11.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
]

rossi_torso_idle_izquierda = girar_imagenes(rossi_torso_idle_derecha, True, False)

rossi_idle_legs_derecha = [
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/idle/legs/4.png").convert_alpha(), (PLAYER_SIZE[2], PLAYER_SIZE[3] * factor_escala))
]

rossi_idle_legs_izquierda = girar_imagenes(rossi_idle_legs_derecha, True, False)

torso_rossi_derecha = [
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/torso_running/0.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/torso_running/1.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/torso_running/2.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/torso_running/3.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/torso_running/4.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/torso_running/5.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/torso_running/6.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/torso_running/7.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/torso_running/8.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/torso_running/9.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/torso_running/10.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1])),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/torso_running/11.png").convert_alpha(), (PLAYER_SIZE[0], PLAYER_SIZE[1]))
]

torso_rossi_izquierda = girar_imagenes(torso_rossi_derecha, True, False)

piernas_rossi_derecha = [
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/legs_running/0.png").convert_alpha(), (PLAYER_SIZE[2], PLAYER_SIZE[3] * factor_escala)),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/legs_running/1.png").convert_alpha(), (PLAYER_SIZE[2], PLAYER_SIZE[3] * factor_escala)),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/legs_running/2.png").convert_alpha(), (PLAYER_SIZE[2], PLAYER_SIZE[3] * factor_escala)),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/legs_running/3.png").convert_alpha(), (PLAYER_SIZE[2], PLAYER_SIZE[3] * factor_escala)),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/legs_running/4.png").convert_alpha(), (PLAYER_SIZE[2], PLAYER_SIZE[3] * factor_escala)),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/legs_running/5.png").convert_alpha(), (PLAYER_SIZE[2], PLAYER_SIZE[3] * factor_escala)),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/legs_running/6.png").convert_alpha(), (PLAYER_SIZE[2], PLAYER_SIZE[3] * factor_escala)),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/legs_running/7.png").convert_alpha(), (PLAYER_SIZE[2], PLAYER_SIZE[3] * factor_escala)),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/legs_running/8.png").convert_alpha(), (PLAYER_SIZE[2], PLAYER_SIZE[3] * factor_escala)),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/legs_running/9.png").convert_alpha(), (PLAYER_SIZE[2], PLAYER_SIZE[3] * factor_escala)),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/legs_running/10.png").convert_alpha(), (PLAYER_SIZE[2], PLAYER_SIZE[3] * factor_escala)),
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/legs_running/11.png").convert_alpha(), (PLAYER_SIZE[2], PLAYER_SIZE[3] * factor_escala))
]

piernas_rossi_izquierda = girar_imagenes(piernas_rossi_derecha, True, False)

rossi_saltando_derecha = [
    pygame.transform.scale(pygame.image.load("./assets/images/main_player/player_jump/0.png").convert_alpha(), (PLAYER_SIZE[0], (PLAYER_SIZE[1] + PLAYER_SIZE[3]) * factor_escala)),
]

rossi_saltando_izquierda = girar_imagenes(rossi_saltando_derecha, True, False)

imagen_transparente = pygame.Surface((PLAYER_SIZE[2], PLAYER_SIZE[3] * factor_escala))
imagen_transparente.fill(RED)
imagen_transparente.set_colorkey(RED)

lista_imagenes_transparentes = [
    imagen_transparente
]

nivel_4 = [
    pygame.transform.scale(pygame.image.load("./images/nivel4/0.png").convert(), (SCREEN_SIZE[0], SCREEN_SIZE[0])),
    pygame.transform.scale(pygame.image.load("./images/nivel4/0.png").convert(), (SCREEN_SIZE[0], 50)),
    pygame.transform.scale(pygame.image.load("./images/nivel4/0.png").convert(), (PLAYER_SIZE[0], (PLAYER_SIZE[1] + PLAYER_SIZE[3]) * factor_escala)),
]

backgrounds = [
    pygame.image.load("./images/tilesmaps/backgrounds/city-ruins.png").convert(),
    pygame.image.load("./images/tilesmaps/backgrounds/hills.png").convert(),
    pygame.image.load("./images/tilesmaps/backgrounds/jungle.png").convert(),
    pygame.image.load("./images/tilesmaps/backgrounds/spooky.png").convert(),
]

platforms_level_1 = [
    pygame.image.load("./images/tilesmaps/tilejungle/0.png").convert_alpha(),
    pygame.image.load("./images/tilesmaps/tilejungle/1.png").convert_alpha(),
    pygame.image.load("./images/tilesmaps/tilejungle/2.png").convert_alpha(),
    pygame.image.load("./images/tilesmaps/tilejungle/3.png").convert_alpha(),
    pygame.image.load("./images/tilesmaps/tilejungle/4.png").convert_alpha(),
    pygame.image.load("./images/tilesmaps/tilejungle/5.png").convert_alpha(),
    pygame.image.load("./images/tilesmaps/tilejungle/6.png").convert_alpha(),
    pygame.image.load("./images/tilesmaps/tilejungle/7.png").convert_alpha(),
    pygame.image.load("./images/tilesmaps/tilejungle/8.png").convert_alpha()
]

platforms_level_2 = [
    pygame.image.load("./assets/images/map/hell/0.png").convert_alpha(),
    pygame.image.load("./assets/images/map/hell/1.png").convert_alpha(),
    pygame.image.load("./assets/images/map/hell/2.png").convert_alpha(),
]

platforms_level_3 = [
    pygame.image.load("./assets/images/map/piedras/0.png").convert_alpha(),
    pygame.image.load("./assets/images/map/piedras/1.png").convert_alpha(),
    pygame.image.load("./assets/images/map/piedras/2.png").convert_alpha(),
]

shield_enemy_izquierda = [
    pygame.transform.scale(pygame.image.load("./assets/images/enemies/shield_enemy/0.png").convert_alpha(), (PLAYER_WIDTH, PLAYER_HEIGHT)),
    pygame.transform.scale(pygame.image.load("./assets/images/enemies/shield_enemy/1.png").convert_alpha(), (PLAYER_WIDTH, PLAYER_HEIGHT)),
    pygame.transform.scale(pygame.image.load("./assets/images/enemies/shield_enemy/2.png").convert_alpha(), (PLAYER_WIDTH, PLAYER_HEIGHT)),
    pygame.transform.scale(pygame.image.load("./assets/images/enemies/shield_enemy/3.png").convert_alpha(), (PLAYER_WIDTH, PLAYER_HEIGHT)),
    pygame.transform.scale(pygame.image.load("./assets/images/enemies/shield_enemy/4.png").convert_alpha(), (PLAYER_WIDTH, PLAYER_HEIGHT)),
    pygame.transform.scale(pygame.image.load("./assets/images/enemies/shield_enemy/5.png").convert_alpha(), (PLAYER_WIDTH, PLAYER_HEIGHT)),
    pygame.transform.scale(pygame.image.load("./assets/images/enemies/shield_enemy/6.png").convert_alpha(), (PLAYER_WIDTH, PLAYER_HEIGHT)),
    pygame.transform.scale(pygame.image.load("./assets/images/enemies/shield_enemy/7.png").convert_alpha(), (PLAYER_WIDTH, PLAYER_HEIGHT)),
    pygame.transform.scale(pygame.image.load("./assets/images/enemies/shield_enemy/8.png").convert_alpha(), (PLAYER_WIDTH, PLAYER_HEIGHT)),
    pygame.transform.scale(pygame.image.load("./assets/images/enemies/shield_enemy/9.png").convert_alpha(), (PLAYER_WIDTH, PLAYER_HEIGHT)),
    pygame.transform.scale(pygame.image.load("./assets/images/enemies/shield_enemy/10.png").convert_alpha(),(PLAYER_WIDTH, PLAYER_HEIGHT)),
    pygame.transform.scale(pygame.image.load("./assets/images/enemies/shield_enemy/11.png").convert_alpha(),(PLAYER_WIDTH, PLAYER_HEIGHT))
]

shield_enemy_derecha = girar_imagenes(shield_enemy_izquierda, True, False)

img_item_vida = [
    pygame.image.load("./assets/images/items/vida/0.png").convert_alpha(),
    pygame.image.load("./assets/images/items/vida/1.png").convert_alpha(),
    pygame.image.load("./assets/images/items/vida/2.png").convert_alpha(),
    pygame.image.load("./assets/images/items/vida/3.png").convert_alpha(),
    pygame.image.load("./assets/images/items/vida/4.png").convert_alpha(),
    pygame.image.load("./assets/images/items/vida/5.png").convert_alpha(),
    pygame.image.load("./assets/images/items/vida/6.png").convert_alpha(),
    pygame.image.load("./assets/images/items/vida/7.png").convert_alpha(),
    pygame.image.load("./assets/images/items/vida/8.png").convert_alpha(),
    pygame.image.load("./assets/images/items/vida/9.png").convert_alpha(),
    pygame.image.load("./assets/images/items/vida/10.png").convert_alpha(),
    pygame.image.load("./assets/images/items/vida/11.png").convert_alpha(),
    pygame.image.load("./assets/images/items/vida/12.png").convert_alpha(),
    pygame.image.load("./assets/images/items/vida/13.png").convert_alpha(),
    pygame.image.load("./assets/images/items/vida/14.png").convert_alpha(),
    pygame.image.load("./assets/images/items/vida/15.png").convert_alpha(),
    pygame.image.load("./assets/images/items/vida/16.png").convert_alpha(),
    pygame.image.load("./assets/images/items/vida/17.png").convert_alpha(),
    pygame.image.load("./assets/images/items/vida/18.png").convert_alpha(),
    pygame.image.load("./assets/images/items/vida/19.png").convert_alpha(),
    pygame.image.load("./assets/images/items/vida/20.png").convert_alpha(),

]

# img_trampa = [
#     pygame.image.load("./assets/images/items/trampa/0.png").convert_alpha(),
#     pygame.image.load("./assets/images/items/trampa/1.png").convert_alpha(),
#     pygame.image.load("./assets/images/items/trampa/2.png").convert_alpha(),
#     pygame.image.load("./assets/images/items/trampa/3.png").convert_alpha(),
#     pygame.image.load("./assets/images/items/trampa/4.png").convert_alpha(),
#     pygame.image.load("./assets/images/items/trampa/5.png").convert_alpha(),
#     pygame.image.load("./assets/images/items/trampa/6.png").convert_alpha(),
#     pygame.image.load("./assets/images/items/trampa/7.png").convert_alpha(),
#     pygame.image.load("./assets/images/items/trampa/8.png").convert_alpha(),
#     pygame.image.load("./assets/images/items/trampa/9.png").convert_alpha(),
#     pygame.image.load("./assets/images/items/trampa/10.png").convert_alpha(),
#     pygame.image.load("./assets/images/items/trampa/11.png").convert_alpha(),
# ]

lista_img_trampa_reposo = [
    pygame.image.load("./assets/images/items/trampa/0.png").convert_alpha(),
    pygame.image.load("./assets/images/items/trampa/1.png").convert_alpha(),
    pygame.image.load("./assets/images/items/trampa/2.png").convert_alpha(),
    # pygame.image.load("./assets/images/items/trampa/10.png").convert_alpha(),
    # pygame.image.load("./assets/images/items/trampa/11.png").convert_alpha()
]

lista_img_trampa_activada = [
    pygame.image.load("./assets/images/items/trampa/3.png").convert_alpha(),
    pygame.image.load("./assets/images/items/trampa/4.png").convert_alpha(),
    pygame.image.load("./assets/images/items/trampa/5.png").convert_alpha(),
    pygame.image.load("./assets/images/items/trampa/6.png").convert_alpha(),
    pygame.image.load("./assets/images/items/trampa/7.png").convert_alpha(),
    pygame.image.load("./assets/images/items/trampa/8.png").convert_alpha(),
    pygame.image.load("./assets/images/items/trampa/9.png").convert_alpha(),
    pygame.image.load("./assets/images/items/trampa/10.png").convert_alpha(),
    pygame.image.load("./assets/images/items/trampa/11.png").convert_alpha()
]


sonido_trampa = [
    "./sounds/st2_0A.wav"
]

lista_img_icono_sonido = [
    pygame.image.load("./assets/images/sound_icon/0.png").convert_alpha(),
    pygame.image.load("./assets/images/sound_icon/1.png").convert_alpha(),
    pygame.image.load("./assets/images/sound_icon/2.png").convert_alpha(),
    pygame.image.load("./assets/images/sound_icon/3.png").convert_alpha()
]

def generar_superficie_transparente(ancho: int, alto: int)-> pygame.Surface:
    imagen_transparente = pygame.Surface((ancho, alto))
    imagen_transparente.set_colorkey("black")
    return imagen_transparente

