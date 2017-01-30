import pygame;
import objet;

class Character(Objet):
    def __init__(self, pos_x, pos_y, imgPath, hp, speed):
        Object.__init__(self, pos_x, pos_y, imgPath)
        self.hp = hp;
        self.speed = vitesse;
