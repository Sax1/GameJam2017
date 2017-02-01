import sys
import pygame
import projectile
import util
import physic
import character

def applySort(listSorts,listEntity,height,width):
    for listSort in listSorts:
        seekAndDestroy(listEntity, listSort);
        isOutside(listSort,height,width);
        applyDeplacement(listSort);

def seekAndDestroy(listEntity, listSorts):
    for entity in listEntity:
        for sort in listSorts:
            applyHurting(entity, sort);


def isOutside(listSorts,height,width):
    for sort in listSorts:
        posSort =  sort.get_pos();
        if(posSort[0] <= 0 or posSort[0] >= width or posSort[1] <= 0 or posSort[1] >= height):
            sort.reinitProjectile();

def applyDeplacement(listSorts):
    for sort in listSorts:
        sort.applyDeplacementP();

def launchBoule(dep,listSorts, j):
    i = 0;
    b = 0;
    while(i < len(listSorts) and b == 0):
        if(listSorts[i].present == 0):
            listSorts[i].set_pos((j.get_pos()[0]+j.get_img().get_width()+10),j.get_pos()[1])
            listSorts[i].setDeplacementP(dep[0]*listSorts[i].getSpeed(),dep[1]*listSorts[i].getSpeed())
            listSorts[i].setPresent(1)
            b = 1;
        i = i+1;

def applyHurting(entity, sort):
    centerSort = (sort.get_pos()[0]+sort.get_img().get_width()/2,sort.get_pos()[1]+sort.get_img().get_height()/2);
    if(centerSort[0] > entity.get_pos()[0] and centerSort[0] < entity.get_pos()[0]+entity.get_img().get_width() and centerSort[1] > entity.get_pos()[1] and centerSort[1] < entity.get_pos()[1]+entity.get_img().get_height()):
        entity.setDamage(sort.getDamage());
        sort.reinitProjectile();
