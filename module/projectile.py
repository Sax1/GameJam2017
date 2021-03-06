import sys
import pygame
import sprite;

class Projectile(sprite.Sprite):
    """docstring for ."""
    def __init__(self,pos_x, pos_y, path,speed,deplacement,degat,present,imgTab,typep):
        sprite.Sprite.__init__(self, pos_x, pos_y, path)
        self.imgTab = imgTab
        self.degat = degat
        self.speed = speed
        self.deplacement = deplacement
        self.present = 0
        self.typep = typep
    def setDeplacementP(self,x,y):
        self.deplacement = (x,y)
    def applyDeplacementP(self):
        self.pos_x = self.pos_x+self.deplacement[0]
        self.pos_y = self.pos_y+self.deplacement[1]
    def getDamage(self):
        return self.degat;
    def reinitProjectile(self):
        if(self.present == 1):
            self.deplacement = (0,0);
            self.pos_x = -100;
            self.pos_y = -100;
            self.present = 0;
    def getSpeed(self):
        return self.speed
    def setPresent(self, val):
        self.present = val;
    def getimgTab(self):
        return self.imgTab
    def getTypep(self):
        return self.typep
