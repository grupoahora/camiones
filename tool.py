from typing import Any
import pygame
import const
import math
import random
class Tool():
    def __init__(self, image,image_bullet_hook):
        self.image_bullet_hook = image_bullet_hook
        self.image_tool =  image
        self.angle = 0
        self.image = pygame.transform.rotate(self.image_tool, self.angle)
        self.shape = self.image.get_rect()
        self.fired = False
        self.last_shot = pygame.time.get_ticks()
        
    def update(self, player):
        
        shot_cooldown = const.COLDOWN_SHOT_BULLET
        bullet = None
        self.shape.center = player.shape.center
        #change the position of the hook form the player shape 
        #self.shape.y = player.shape.y + (player.shape.height/2)
        
        if player.fliph == False:
            #self.shape.x = player.shape.x + (player.shape.width/4)
            self.rotate_tool(False)
        if player.fliph == True:
            #self.shape.x = player.shape.x - (player.shape.width/4)
            self.rotate_tool(True)
        if player.flipv == False:
            #self.shape.y = player.shape.y+ (player.shape.height/2)
            self.rotate_tool(False)
        if player.flipv == True:
            #self.shape.y = player.shape.y- (player.shape.height/2)
            self.rotate_tool(True)
        #move hook with mouse
        mouse_pos = pygame.mouse.get_pos()
        distance_x = mouse_pos[0] - self.shape.centerx
        distance_y = -(mouse_pos[1] - self.shape.centery)
        self.angle = math.degrees(math.atan2(distance_y, distance_x))
        #print(self.angle)
        #detecte clicked mouse
        if pygame.mouse.get_pressed()[0] and self.fired == False and (pygame.time.get_ticks() - self.last_shot >= shot_cooldown):
            bullet = Bullet(self.image_bullet_hook,self.shape.centerx,self.shape.centery,self.angle)
            self.fired = True
            self.last_shot = pygame.time.get_ticks()
            
            
        #reset click mouse
        if pygame.mouse.get_pressed()[0] == False:
            self.fired = False
        return bullet
    def rotate_tool(self, rotate):
        if rotate == True:
            image_flip =  pygame.transform.flip(self.image_tool,True, False)
            self.image = pygame.transform.rotate(image_flip, self.angle)

        else:
            image_flip =  pygame.transform.flip(self.image_tool,False, False)
            self.image = pygame.transform.rotate(image_flip, self.angle)
            
    def draw(self, interfaz):
        self.image = pygame.transform.rotate(self.image, self.angle)
        interfaz.blit(self.image, self.shape)
        pygame.draw.rect(interfaz, const.COLOR_TOOL, self.shape, 1)
class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image_bullet = image
        #self.shape = self.image.get_rect()
        #self.shape.center = (x, y)
        self.angle = angle
        self.image = pygame.transform.rotate(self.image_bullet, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        #get speed pf bullet 
        self.delta_x = math.cos(math.radians(self.angle))*const.SPEED_BULLET
        self.delta_y = -math.sin(math.radians(self.angle))*const.SPEED_BULLET

    def update(self, lists_objs):
        self.rect.x = self.rect.x + self.delta_x
        self.rect.y = self.rect.y + self.delta_y
        #validate visualization bullet position
        if self.rect.right < 0 or self.rect.left > const.WIDTH or self.rect.top < 0 or self.rect.bottom > const.HEIGHT:
            self.kill()
        
        #verify if collision detection with objs
        for obj in lists_objs:
            if obj,shape,colliderect(self.rect): 
                daño = 15 + random.randint(-7,7)
                
                
    def draw(self, interfaz):
        interfaz.blit(self.image, (self.rect.centerx, self.rect.centery))