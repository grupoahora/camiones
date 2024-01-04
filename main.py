import pygame
import const
from person import Person
from person import Obj
from tool import Tool
import os

#funciones
#scale images
def scale(image, scale):
    w = image.get_width()
    h = image.get_height()
    new_image = pygame.transform.scale(image, (w*scale, h*scale))
    return new_image

#count elements
def count_elements(dir):
    return len(os.listdir(dir))

#print(f"elementos {count_elements('assets/images/characters/objs')}")
#list name of elements

def name_of_element(dir):
    return os.listdir(dir)
#print(f"elementos {name_of_element('assets/images/characters/objs')}")

pygame.init()
window = pygame.display.set_mode([const.WIDTH, const.HEIGHT])
pygame.display.set_caption("camiones")


#import images

#person
animationsh = []
animationsv = []
for i in range (2):
    #print(i)
    imgh = pygame.image.load(f"assets/images/characters/player/playerh-{i}.png")
    imgh = scale(imgh, const.SCALE_PERSON)
    animationsh.append(imgh)
    imgv = pygame.image.load(f"assets/images/characters/player/playerv-{i}.png")
    imgv = scale(imgv, const.SCALE_PERSON)
    animationsv.append(imgv)
    
#objs

dir_objs = "assets/images/characters/objs"
type_objs = name_of_element(dir_objs)
#print(f"objs- {type_objs}")
animations_objs = []
for obj in type_objs:
    lists_temp = []
    route_temp = f"assets/images/characters/objs/{obj}"
    num_animations = count_elements(route_temp)
    #print(f"objs- {num_animations}")
    for i in range(num_animations):
        image_obj = pygame.image.load(f"{route_temp}/{obj}_{i}.png")
        image_obj = scale(image_obj, const.SCALE_OBJ)
        lists_temp.append(image_obj)
    animations_objs.append(lists_temp)
#print(animations_objs)
#image init
player_imageh = pygame.image.load("assets/images/characters/player/playerh-0.png")
player_imageh = scale(player_imageh, const.SCALE_PERSON)
player_imagev = pygame.image.load("assets/images/characters/player/playerv-0.png")
player_imagev = scale(player_imagev, const.SCALE_PERSON)
image_hook = pygame.image.load("assets/images/tools/hook.png")
image_hook = scale(image_hook, const.SCALE_TOOL)
#imagebullet hook
image_bullet_hook = pygame.image.load("assets/images/tools/hookbullet.png")
image_bullet_hook = scale(image_bullet_hook, const.SCALE_BULLETS_TOOL)



#create the player
player = Person(400, 750, animationsh, animationsv, 100)


#create the obj
obj_dirt0 = Obj(200, 700, animations_objs[0], 100)
obj_dirt1 = Obj(400, 700, animations_objs[0], 100)
obj_fungi0 = Obj(500, 700, animations_objs[1], 100)
obj_fungi1 = Obj(300, 700, animations_objs[1], 100)

#create list of objs

lists_objs = []
lists_objs.append(obj_dirt0)
lists_objs.append(obj_dirt1)
lists_objs.append(obj_fungi0)
lists_objs.append(obj_fungi1)
#print(lists_objs)
#create to tool for get dirt
hook = Tool(image_hook, image_bullet_hook)

#create gruop the sprites
group_bullet = pygame.sprite.Group()
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
    
    #move to player
    player.move(delta_x, delta_y)
    # Mover al jugador solo si hay un cambio en las coordenadas
    if delta_x != 0 or delta_y != 0:
        player.move(delta_x, delta_y)
        if delta_x != 0:
            player.updateh()
        if delta_y != 0:
            player.updatev()
    
    #update state of obj
    for obj in lists_objs:
       obj.update()
       print(obj.energy)
   
    # draw of player
    player.draw(window)
    
    #draw of obj
    for obj in lists_objs:
        obj.draw(window)
    # Actualizar y dibujar el gancho encima del jugador
    bullet = hook.update(player)
    
   
    if bullet:
        group_bullet.add(bullet)
    for bullet in group_bullet:
        bullet.update(lists_objs)
        
    #print(group_bullet)
    
    #draw tool
    
    hook.draw(window)
    
    #draw bullet
    for bullet in group_bullet:
        bullet.draw(window)
        
    
    
    

   

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