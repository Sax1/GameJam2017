import sys
import pygame
import sprite;
import projectile


def listeboulefeu():
    listboulefeu = [];
    for i in range(0,20):
        listboulefeu.append(projectile.Projectile(i,None,None,'./data/bouledefeu.png',"feu",10))
    for i in range(0,20):
        print(listboulefeu[i])
    return listboulefeu
