import pygame;
import sprite;

class Character(sprite.Sprite):
    def __init__(self, pos_x, pos_y, imgPath, hp, speed, statut):
        sprite.Sprite.__init__(self, pos_x, pos_y, imgPath)
        self.hp = hp;
        self.speed = speed;
        self.gravity = 1;
        self.alive = 1;
        self.ascend = 0;
        self.ascendValue = 0;
        self.landed = 0;
        self.jump = 0;
        self.statut = "";

    def set_hp(self,newHP):
        self.hp = newHP;
    def set_vitesse(self,newVitesse):
        self.speed = newVitesse;
    def get_hp(self):
        return self.hp;
    def get_vitesse(self):
        return self.speed;
    def changeHealth(self, value):
        self.hp =  self.hp + value;
    def setGravity(self, state):
        self.gravity = state;
    def getGravity(self):
        return self.gravity;
    def setDeplacement(self, x,y):
        self.pos_x = (self.pos_x + x*self.speed);
        self.pos_y = (self.pos_y + y);
    def getBottemChar(self):
        return ((self.pos_x+self.image.get_height(),self.pos_y+self.image.get_width()/2))
    def setDamage(self, dmg):
        self.hp = self.hp + dmg;
    def isDead(self):
        if(self.alive == 1 and self.hp <= 0):
            self.alive = 0;
            self.set_pos(-500,-500);
            return 1;
        else:
            return 0;
    def getAscend(self):
        return self.ascend;
    def setAscendValue(self, value):
        self.ascendValue = value;
    def getAscendValue(self):
        return self.ascendValue;
    def getLanded(self):
        return self.landed;
    def setAscend(self, state):
        self.ascend = state;
    def setLanded(self, state):
        self.landed = state;
    def setJump(self,state):
        self.jump = state;
    def getJump(self):
        return self.jump;
    def jump(self):
        self.setLanded(0);
        self.setAscend(1);
    def setStatut (self, newStatut):
        self.statut = newStatut;
    def getStatut (self):
        return self.statut;
