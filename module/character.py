import pygame;
import objet;

class Character(Objet):
    def __init__(self, pos_x, pos_y, imgPath, hp, speed):
        Object.__init__(self, pos_x, pos_y, imgPath)
        self.hp = hp;
        self.speed = vitesse;

    def set_hp(self,newHP):
        self.hp = newHP;
    def set_vitesse(self,newVitesse):
        self.vitesse = newVitesse;
    def get_hp(self):
        return self.hp;
    def get_vitesse(self):
        return self.speed;
    def changeHealth(self, value):
        self.hp =  hp + value;
