import pygame
import const
class Person():
    def __init__(self, x, y, image):
        self.fliph = False
        self.flipv = False
        self.image = image
        self.imageh = image
    
        # Calculamos las nuevas dimensiones manteniendo las proporciones
        self.nuevo_ancho = int(self.image.get_width() * const.SCALE_PERSON)
        self.nuevo_alto = int(self.image.get_height() * const.SCALE_PERSON)

        # Escalamos la imagen con las nuevas dimensiones
        self.shape = pygame.Rect(0,0,const.WIDTH_PERSON,const.HEIGHT_PERSON)
        self.shape.center =  (x,y)
    
    def draw(self, interfaz):
        self.image = pygame.transform.scale(self.image, (self.nuevo_ancho, self.nuevo_alto))
        imagen_flip = pygame.transform.flip(self.image, self.fliph, self.flipv)
        interfaz.blit(imagen_flip, self.shape)
        #pygame.draw.rect(interfaz, const.COLOR_PERSON, self.shape)
    def move(self, delta_x, delta_y):
        if delta_x < 0:
            self.image = self.imageh
            # Calculamos las nuevas dimensiones manteniendo las proporciones
            self.nuevo_ancho = int(self.image.get_width() * const.SCALE_PERSON)
            self.nuevo_alto = int(self.image.get_height() * const.SCALE_PERSON)
            
            self.fliph = True
        if delta_x > 0:
            self.image = self.imageh
            # Calculamos las nuevas dimensiones manteniendo las proporciones
            self.nuevo_ancho = int(self.image.get_width() * const.SCALE_PERSON)
            self.nuevo_alto = int(self.image.get_height() * const.SCALE_PERSON)
            
            self.fliph = False
        if delta_y < 0:
            self.image = pygame.image.load("assets/images/characters/player/playerv-0.png")
            # Calculamos las nuevas dimensiones manteniendo las proporciones
            self.nuevo_ancho = int(self.image.get_width() * const.SCALE_PERSON)
            self.nuevo_alto = int(self.image.get_height() * const.SCALE_PERSON)
            self.flipv = False

        if delta_y > 0:
            self.image = pygame.image.load("assets/images/characters/player/player-3.png")
            # Calculamos las nuevas dimensiones manteniendo las proporciones
            self.nuevo_ancho = int(self.image.get_width() * const.SCALE_PERSON)
            self.nuevo_alto = int(self.image.get_height() * const.SCALE_PERSON)

            self.flipv = True

        self.shape.x = self.shape.x + delta_x
        self.shape.y = self.shape.y + delta_y
