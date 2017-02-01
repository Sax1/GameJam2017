import sys
import pygame
import sprite;
import projectile
import squelette


def listeboulefeu():
    listboulefeu = [];
    for i in range(0,100):
        listboulefeu.append(projectile.Projectile(-100,-100,'./data/minibouboule.png',20,(0,0),"feu",-10,0))
    return listboulefeu


def listeskelet():
    listeskelet = [];
    for i in range(0,50):
        listeskelet.append(squelette.Squelette(450,50,'./sprite/Skeleton/skeletonDR-1.png', 30, 0.5, " ", 15))
    return listeskelet
