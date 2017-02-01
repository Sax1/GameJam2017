import pygame;
import mobs;


class Squelette(mobs.Mobs):
    def __init__(self, pos_x, pos_y, imgPath, hp, speed, statut, damages):
        mobs.Mobs.__init__(self, pos_x, pos_y, imgPath, hp, speed, statut, damages)
        self.damages = 15;
