import pygame;
import character;

class Mobs(character.Character):
    def __init__(self, pos_x, pos_y, imgPath, hp, speed, statut, damages):
        character.Character.__init__(self, pos_x, pos_y, imgPath, hp, speed, statut)
        self.damages = damages;


    def setDamages (self, newDamages):
        self.damages = newDamages;
    def getDamages (self):
        return self.damages;
