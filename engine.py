from level_1 import Level1
from level_2 import Level2
from menu import Menu
import pygame

class Engine:
    def __init__(self):
        self.LEVEL_1 = False
        self.LEVEL_2 = False
        self.MENU = False
    
    def setLevel1(self):
        self.LEVEL_1 = True
    
    def setLevel2(self):
        self.LEVEL_2 = True
    
    def setMenu(self):
        self.MENU = True
    def stopMenu(self):
        self.MENU = False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.setMenu()

            if self.MENU:
                MENU = Menu()
                self.stopMenu()

                if MENU.LEVEL_1_RUN:
                    self.setLevel1()
                if MENU.LEVEL_2_RUN:
                    self.setLevel2()
                MENU.run()
                
            
            LEVEL_1 = Level1()
            if LEVEL_1.PLAY == False:
                self.setMenu()

            


if __name__ == "__main__":
    pygame.init()
    ENGINE = Engine()
    ENGINE.run()

   
   
