import pygame
import const
class Person():
    def __init__(self, x, y, animationsh,animationsv, energy):
        self.fliph = False
        self.flipv = False
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = animationsh[self.frame_index]
        self.imagev = animationsv[self.frame_index]
        self.imageh = animationsh[self.frame_index]
        self.animationsh = animationsh
        self.animationsv = animationsv
        self.energy = energy
    
        
        # Inicializamos el rectángulo con las dimensiones de la primera imagen
        self.shape = self.image.get_rect(topleft=(x, y))
        self.shape.center =  (x,y)
    
    def draw(self, interfaz):
        
        imagen_flip = pygame.transform.flip(self.image, self.fliph, self.flipv)
        interfaz.blit(imagen_flip, self.shape)
        pygame.draw.rect(interfaz, const.COLOR_PERSON, self.shape, 1)
    def update_rect(self):
        # Actualizamos el rectángulo con las dimensiones de la imagen actual
        self.shape = self.image.get_rect(center=self.shape.center)
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
        # Actualizamos el rectángulo al cambiar la imagen
        self.update_rect()
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
            
class Obj():
    def __init__(self, x, y, animations, energy):
        self.flip = False
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = animations[self.frame_index]
         # Inicializamos el rectángulo con las dimensiones de la primera imagen
        self.shape = self.image.get_rect(topleft=(x, y))
        self.shape.center =  (x,y)
        self.animations = animations
        self.energy = energy
        
    def draw(self, interfaz):
        interfaz.blit(self.image, self.shape)
        pygame.draw.rect(interfaz, const.COLOR_PERSON, self.shape, 1)
    def update(self):
        cooldown_animation = const.SPEED_ANIMATION_PERSON
        self.image = self.animations[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > cooldown_animation:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
            
        if self.frame_index >= len(self.animations):
            self.frame_index = 0
        