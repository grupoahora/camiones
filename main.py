import pygame
import const
from person import Person
pygame.init()
window = pygame.display.set_mode([const.WIDTH, const.HEIGHT])
pygame.display.set_caption("camiones")

def scale(image, scale):
    w = image.get_width()
    h = image.get_height()
    new_image = pygame.transform.scale(image, (w*scale, h*scale))
    return new_image
#Animiaciones
animationsh = []
animationsv = []
for i in range (2):
    print(i)
    imgh = pygame.image.load(f"assets/images/characters/player/playerh-{i}.png")
    imgh = scale(imgh, const.SCALE_PERSON)
    animationsh.append(imgh)
    imgv = pygame.image.load(f"assets/images/characters/player/playerv-{i}.png")
    imgv = scale(imgv, const.SCALE_PERSON)
    animationsv.append(imgv)
player_imageh = pygame.image.load("assets/images/characters/player/playerh-0.png")
player_imageh = scale(player_imageh, const.SCALE_PERSON)
player_imagev = pygame.image.load("assets/images/characters/player/playerv-0.png")
player_imagev = scale(player_imagev, const.SCALE_PERSON)
player = Person(400, 750, animationsh, animationsv)
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
    # Mover al jugador solo si hay un cambio en las coordenadas
    if delta_x != 0 or delta_y != 0:
        player.move(delta_x, delta_y)
        if delta_x != 0:
            player.updateh()
        if delta_y != 0:
            player.updatev()
    
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