import pygame;
import sprite;

class Character(sprite.Sprite):
    def __init__(self, pos_x, pos_y, imgPath, hp, speed):
        sprite.Sprite.__init__(self, pos_x, pos_y, imgPath)
        self.hp = hp;
        self.speed = speed;
        self.gravity = 1;

    def set_hp(self,newHP):
        self.hp = newHP;
    def set_vitesse(self,newVitesse):
        self.speed = newVitesse;
    def get_hp(self):
        return self.hp;
    def get_vitesse(self):
        return self.speed;
    def changeHealth(self, value):
        self.hp =  hp + value;
    def setGravity(self, state):
        self.gravity = state;
    def getGravity(self):
        return gravity;
    def setDeplacement(self, x,y):
        self.pos_x = (self.pos_x + x)*self.speed;
        self.pos_y = (self.pos_y + y);
    def getBottemChar(self):
        return ((self.pos_x+self.image.get_height(),self.pos_y+self.image.get_width()/2))
