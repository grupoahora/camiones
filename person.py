import pygame
import const
class Person():
    def __init__(self, x, y, animationsh,animationsv):
        self.fliph = False
        self.flipv = False
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = animationsh[self.frame_index]
        self.imagev = animationsv[self.frame_index]
        self.imageh = animationsh[self.frame_index]
        self.animationsh = animationsh
        self.animationsv = animationsv
    
        
        # Escalamos la imagen con las nuevas dimensiones
        self.shape = pygame.Rect(0,0,const.WIDTH_PERSON,const.HEIGHT_PERSON)
        self.shape.center =  (x,y)
    
    def draw(self, interfaz):
        
        imagen_flip = pygame.transform.flip(self.image, self.fliph, self.flipv)
        interfaz.blit(imagen_flip, self.shape)
        #pygame.draw.rect(interfaz, const.COLOR_PERSON, self.shape)
    def move(self, delta_x, delta_y):
        if delta_x < 0:
            self.image = self.imageh
            self.fliph = True
        if delta_x > 0:
            self.image = self.imageh
            self.fliph = False
        if delta_y < 0:
            self.image = self.imagev
            self.flipv = False

        if delta_y > 0:
            self.image = self.imagev
            self.flipv = True

        self.shape.x = self.shape.x + delta_x
        self.shape.y = self.shape.y + delta_y
    def updateh(self):
        cooldown_animationh = const.SPEED_ANIMATION_PERSON
        self.image = self.animationsh[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animationh:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animationsh):
            self.frame_index = 0
    def updatev(self):
        cooldown_animationv = const.SPEED_ANIMATION_PERSON
        self.image = self.animationsv[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animationv:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animationsv):
            self.frame_index = 0