import sys;
import pygame;
from pygame.locals import *;
import physic;
import util;
import magic;
import projectile;
import mobs;
import mouvement;
import levels;


def launch(window,listBG, listHUD, listDecors, listPlayers, listEnnemis, gravity, playerDeplacement, nbJoueur, ascendDecrement,listSorts,height,width,listCombo,keysPressed,listHUDPV):
    levels.loadLevel(1,listDecors);
    #pygame.mixer.music.load("./data/Musiques/whatIsLove.mp3");
    #pygame.mixer.music.play();
    while 1:
        listPlayers[0].set_image("./sprite/Joueur1/MageAV-1.png");
        if(nbJoueur == 2):
            listPlayers[1].set_image("./sprite/Joueur2/Mage2AV-1.png");
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed();
                if( event.key == 27):
                    sys.exit();
                else:
                    mouvement.keyPressedDown(keys,listPlayers, nbJoueur, listDecors, listSorts,keysPressed);
            if event.type == pygame.KEYUP:
                mouvement.keyPressedUp(event.key,listPlayers, nbJoueur, listDecors,keysPressed);

        for player in listPlayers:
            mouvement.applyDeplacement(keysPressed, player, listDecors, playerDeplacement);
            physic.applyGravity(player, gravity);
            physic.applyCollisionWithFloor(player, listDecors);
            physic.applyJump(player, ascendDecrement);
            physic.jumpCollide(player, listDecors);
        magic.applySort(listSorts,listPlayers,height,width,listCombo)


        #for mobs in listEnnemis:
        for squelette in listEnnemis[0]:
            if(not squelette.isDead()):
                physic.applyGravity(squelette, gravity);
                physic.applyCollisionWithFloor(squelette, listDecors);
                physic.applyJump(squelette, ascendDecrement);
                physic.jumpCollide(squelette, listDecors);
                if(len(listPlayers) == 2):
                    if ( (abs(squelette.pos_x-listPlayers[0].pos_x)) < (abs(squelette.pos_x-listPlayers[1].pos_x)) ):
                        jCible = listPlayers[0];
                    else:
                        jCible = listPlayers[1];
                    if (squelette.pos_x < jCible.pos_x):
                        squelette.setDeplacement(6,0);
                    elif (squelette.pos_x > jCible.pos_x):
                        squelette.setDeplacement(-6,0);
                else:
                    jCible = listPlayers[0];
                    if (squelette.pos_x < jCible.pos_x):
                        squelette.setDeplacement(6,0);
                    elif (squelette.pos_x > jCible.pos_x):
                        squelette.setDeplacement(-6,0);

        magic.applySort(listSorts,listEnnemis[0],height,width,listCombo)
        for e in pygame.event.get():
            if(e.type == pygame.USEREVENT):
                for combos in listCombo:
                    for combo in combos:
                        combo.reinitProjectile()


        for squelette in listEnnemis[1]:
            if(not squelette.isDead()):
                physic.applyGravity(squelette, gravity);
                physic.applyCollisionWithFloor(squelette, listDecors);
                physic.applyJump(squelette, ascendDecrement);
                physic.jumpCollide(squelette, listDecors);
                if(len(listPlayers) == 2):
                    if ( (abs(squelette.pos_x-listPlayers[0].pos_x)) < (abs(squelette.pos_x-listPlayers[1].pos_x)) ):
                        jCible = listPlayers[0];
                    else:
                        jCible = listPlayers[1];
                    if (squelette.pos_x < jCible.pos_x):
                        squelette.setDeplacement(6,0);
                    elif (squelette.pos_x > jCible.pos_x):
                        squelette.setDeplacement(-6,0);
                else:
                    jCible = listPlayers[0];
                    if (squelette.pos_x < jCible.pos_x):
                        squelette.setDeplacement(6,0);
                    elif (squelette.pos_x > jCible.pos_x):
                        squelette.setDeplacement(-6,0);
        magic.applySort(listSorts,listEnnemis[1],height,width,listCombo)


        for squelette in listEnnemis[2]:
            if(not squelette.isDead()):
                physic.applyGravity(squelette, gravity);
                physic.applyCollisionWithFloor(squelette, listDecors);
                physic.applyJump(squelette, ascendDecrement);
                physic.jumpCollide(squelette, listDecors);
                if(len(listPlayers) == 2):
                    if ( (abs(squelette.pos_x-listPlayers[0].pos_x)) < (abs(squelette.pos_x-listPlayers[1].pos_x)) ):
                        jCible = listPlayers[0];
                    else:
                        jCible = listPlayers[1];
                    if (squelette.pos_x < jCible.pos_x):
                        squelette.setDeplacement(6,0);
                    elif (squelette.pos_x > jCible.pos_x):
                        squelette.setDeplacement(-6,0);
                else:
                    jCible = listPlayers[0];
                    if (squelette.pos_x < jCible.pos_x):
                        squelette.setDeplacement(6,0);
                    elif (squelette.pos_x > jCible.pos_x):
                        squelette.setDeplacement(-6,0);
        magic.applySort(listSorts,listEnnemis[2],height,width,listCombo)



        if(listPlayers[0].isDead()):
            break;
        elif(nbJoueur == 2 and listPlayers[1].isDead()):
            break;


        #display all the element on screen
        util.displayAllImages(window, listBG);
        util.displayAllImages(window, listPlayers);
        for listElem in listSorts:
            util.displayAllImages(window, listElem);
        util.displayAllImages(window, listDecors);
        util.displayAllImages(window, listEnnemis[0]);
        util.displayAllImages(window, listEnnemis[1]);
        util.displayAllImages(window, listEnnemis[2]);
        listHUDPVact = []
        listHUDPVact.append(util.setHUDPV(listHUDPV[0][2],listHUDPV[0][3],listHUDPV[0][4]))
        if(len(listHUDPV) ==2):
            listHUDPVact.append(util.setHUDPV(listHUDPV[1][2],listHUDPV[1][3],listHUDPV[1][4]))
        util.displayAllImages(window, listHUD);
        util.displayAllPv(window,listHUDPVact);
        for Combo in listCombo:
            util.displayAllImages(window, Combo);


        pygame.display.flip();
