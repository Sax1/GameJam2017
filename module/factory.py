import sys
import pygame
import sprite;
import projectile
import squelette


def listeboulefeu(imgTab):
    print imgTab;
    print imgTab[0];
    listboulefeu = [];
    for i in range(0,20):
        listboulefeu.append(projectile.Projectile(-100,-100,imgTab[0],20,(0,0),-10,0,imgTab))
    return listboulefeu

def listePicGlace(imgTab):
    listePicGlace = []
    for i in range(0,20):
        listePicGlace.append(projectile.Projectile(-100,-100,imgTab[0],30,(0,0),-5,0,imgTab))
    return listePicGlace

def listeVent(imgTab):
    listeVent = []
    for i in range(0,20):
        listeVent.append(projectile.Projectile(-100,-100,imgTab[0],5,(0,0),-20,0,imgTab))
    return listeVent

def listeskelet(x, y):
    listeskelet = [];
    for i in range(0,5):
        listeskelet.append(squelette.Squelette(x,y,'./sprite/Skeleton/skeletonDR-1.png', 30, 0.5, " ", 15))
    return listeskelet
