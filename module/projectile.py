import sys
import pygame
import sprite;

class Projectile(sprite.Sprite):
    """docstring for ."""
    def __init__(self, index,pos_x, pos_y, imgPath,typep,degat):
        sprite.Sprite.__init__(self, pos_x, pos_y, imgPath)
        self.degat = degat
        self.index = index
        self.typep = typep
    def __str__(self):
        return "projectile {} de {} qui fait {} de degats".format(self.index,self.typep,self.degat)
