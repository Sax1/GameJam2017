import sys
import pygame
import sprite;
import projectile


def listeboulefeu():
    listboulefeu = [];
    for i in range(0,100):
        listboulefeu.append(projectile.Projectile(-100,-100,'./data/minibouboule.png',20,(0,0),"feu",-10,0))
    return listboulefeu
