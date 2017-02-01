import sys
import pygame
import sprite;
import projectile


def listeboulefeu(imgTab):
    listboulefeu = [];
    for i in range(0,100):
        listboulefeu.append(projectile.Projectile(-100,-100,imgTab,15,(0,0),-10,0))
    return listboulefeu

def listePicGlace():
    listePicGlace = []
    for i in range(0,20):
        listePicGlace.append(projectile.Projectile(-100,-100,imgTab,30,(0,0),-5,0))
    return listePicGlace

def listeVent():
    listeVent = []
    for i in range(0,20):
        listeVent.append(projectile.Projectile(-100,-100,imgTab,5,(0,0),-20,0))
    return listeVent
