import pygame
from pygame.sprite import Sprite
import os

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #loading the image
        current_path = os.path.dirname(__file__) # Where your .py file is located
        resource_path = os.path.join(current_path, '') # The resource folder path
        image_path = os.path.join(resource_path, '') # The image folder path
        
        self.image = pygame.image.load((os.path.join(image_path, 'alien.png'))).convert_alpha()
        # resize the image
        self.image = pygame.transform.scale(self.image, (60, 60))
        
        
        #self.image = pygame.image.load('images/alien.png')
        '''def load_all_gfx(directory, colorkey=(255,0,255),accept=(".png",".jpg",".bmp")):
            graphics = {}
            for pic in os.listdir(directory):
                name,ext = os.path.splitext(pic)
                if ext.lower() in accept:
                    img = pg.image.load(os.path.join(directory,pic))
                    if img.get_alpha():
                        img = img.convert_alpha()
                    else:
                        img = img.convert()
                        img.set_colorkey(colorkey)
                    graphics[name]=img
            return graphics'''
    
            




        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True    

    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x   