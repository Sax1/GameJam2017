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

def launchBoule(dep,listSorts, j,direction):
    i = 0;
    b = 0;
    while(i < len(listSorts) and b == 0):
        if(listSorts[i].present == 0):
            listSorts[i].set_image(listSorts[i].getimgTab()[direction])
            setPosFromDir(j,listSorts[i], direction);
            listSorts[i].setDeplacementP(dep[0]*listSorts[i].getSpeed(),dep[1]*listSorts[i].getSpeed())
            listSorts[i].setPresent(1)
            b = 1;
        i = i+1;

def applyHurting(entity, sort):
    centerSort = (sort.get_pos()[0]+sort.get_img().get_width()/2,sort.get_pos()[1]+sort.get_img().get_height()/2);
    if(centerSort[0] > entity.get_pos()[0] and centerSort[0] < entity.get_pos()[0]+entity.get_img().get_width() and centerSort[1] > entity.get_pos()[1] and centerSort[1] < entity.get_pos()[1]+entity.get_img().get_height()):
        entity.setDamage(sort.getDamage());
        sort.reinitProjectile();

def setPosFromDir(j, sort, dir):
    centreJoueur = (j.get_pos()[0]+j.get_img().get_width()/2,j.get_pos()[1]+j.get_img().get_height()/2)
    demiJX = j.get_img().get_width()/2;
    demiJY = j.get_img().get_height()/2;
    sortImgWidth2 = sort.get_img().get_width()/2;
    sortImgHeight2 = sort.get_img().get_height()/2;
    if(dir == 0):
        sort.set_pos(centreJoueur[0]+demiJX+2,centreJoueur[1]);
    elif(dir == 1):
        sort.set_pos(centreJoueur[0]+demiJX+2,centreJoueur[1]+demiJY+2);
    elif(dir == 2):
        sort.set_pos(centreJoueur[0]-sortImgWidth2,centreJoueur[1]+demiJY+2);
    elif(dir == 3):
        sort.set_pos(centreJoueur[0]-demiJX-2,centreJoueur[1]+demiJY+2);
    elif(dir == 4):
        sort.set_pos(centreJoueur[0]-demiJX-2-2*sortImgWidth2,centreJoueur[1]);
    elif(dir == 5):
        sort.set_pos(centreJoueur[0]-demiJX-2-2*sortImgWidth2,centreJoueur[1]-demiJY-5);
    elif(dir == 6):
        sort.set_pos(centreJoueur[0],centreJoueur[1]-demiJY-2-2*sortImgHeight2);
    elif(dir == 7):
        sort.set_pos(centreJoueur[0]+demiJX+2-sortImgWidth2,centreJoueur[1]-demiJY-2);
