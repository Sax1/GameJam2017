import sys
import pygame
import sprite;
import projectile


def listeboulefeu():
    listboulefeu = [];
    for i in range(0,20):
        listboulefeu.append(projectile.Projectile(None,None,'./data/bouledefeu.png',2,(0,0),"feu",10,0))
    for i in range(0,20):
        print(listboulefeu[i])
    return listboulefeu
