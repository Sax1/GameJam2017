import pygame;
import util;

class Sprite():
    # constructeur
    def __init__(self, pos_x, pos_y, imgPath):
        #initialisations et affectations d'attributs :
        self.pos_x = pos_x;
        self.pos_y = pos_y;
        self.image = util.load_image(imgPath);
        self.rect = pygame.Rect(500, 500, self.image.get_width(), self.image.get_height());

    def get_rect(self):
        return self.rect;

    def get_img(self):
        return self.image;

    def get_pos(self):
        return (self.pos_x,self.pos_y);

    def set_pos(self, x, y):
        self.pos_x = x;
        self.pos_y = y;
