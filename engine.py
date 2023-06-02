from level_1 import Level1
from level_2 import Level2
from menu import Menu
import pygame

class Engine:
    def __init__(self):
        self.GAME_MENU = True

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            if self.GAME_MENU:
                pass

   


if __name__ == "__main__":
    pygame.init()
    ENGINE = Engine()
    ENGINE.run()

   
   
