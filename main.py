import pygame
import const
from person import Person
pygame.init()
window = pygame.display.set_mode([const.WIDTH, const.HEIGHT])
pygame.display.set_caption("camiones")

def
#Animiaciones
animaciones = []
for i in range (2):
    print(i)
    img = pygame.image.load(f"assets/images/characters/player/playerh-{i}.png")
player_image = pygame.image.load("assets/images/characters/player/playerh-1.png")
player = Person(400, 750, player_image)
#definir variables de movimiento
move_top = False
move_down = False
move_left =  False
move_right = False
#controller framerate
clock = pygame.time.Clock()
run = True
while run == True:
    window.fill(const.COLOR_BG)
    #calcular movimiento del jugador
    #set framerate
    clock.tick(const.FPS)
    delta_x = 0
    delta_y = 0
    if move_right == True:
        delta_x =  const.SPEED
    if move_left == True:
        delta_x =  -const.SPEED
    if move_top == True:
        delta_y =  -const.SPEED
    if move_down == True:
        delta_y =  const.SPEED
    #print(f"{delta_x}. {delta_y}")
    #move to player
    player.move(delta_x, delta_y)
    player.draw(window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_w:
                move_top = True
            if event.key == pygame.K_s:
                move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_w:
                move_top = False
            if event.key == pygame.K_s:
                move_down = False
    pygame.display.update()
pygame.quit()