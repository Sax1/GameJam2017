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
<<<<<<< HEAD
    def getAscend(self):
        return self.ascend;
    def getLanded(self):
        return self.landed;
    def setAscend(self, state):
        self.ascend = state;
    def setLanded(self, state):
        self.landed = state;
    def jump(self):
        self.setLanded(0);
        self.setAscend(1);
    def setAscendValue(self, value):
        self.ascendValue = value;
    def getAscendValue(self):
        return self.ascendValue;
    def changeSort(self,val):
        if (val == 1):
            self.sortCourant = (self.sortCourant+val)%3
        elif (val == -1):
            if(self.sortCourant == 0):
                self.sortCourant = 2
            else:
                self.sortCourant = self.sortCourant+val
=======
>>>>>>> bc3e92971c38bd4e61a55c3bd0b638b03226df43
