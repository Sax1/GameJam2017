import sys
import pygame
import sprite;
import projectile


def listeboulefeu():
    listboulefeu = [];
    for i in range(0,20):
        listboulefeu.append(projectile.Projectile(-100,-100,'./data/bouledefeu.png',2,(0,0),"feu",10,0))
    return listboulefeu
