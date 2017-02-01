import pygame;
import character;

class Player(character.Character):
    def __init__(self, pos_x, pos_y, imgPath, hp, speed, numPlayer, listSorts):
        character.Character.__init__(self, pos_x, pos_y, imgPath, hp, speed)
        self.numPlayer = numPlayer;
        self.sorts = listSorts;
        self.sortCourant = 0;


    def setSorts(self, newSorts):
        self.sorts = newSorts;
    def getSorts(self):
        return self.sorts;
    def changeSort(self,val):
        if (val == 1):
            self.sortCourant = (self.sortCourant+val)%3
        elif (val == -1):
            if(self.sortCourant == 0):
                self.sortCourant = 2
            else:
                self.sortCourant = self.sortCourant+val
