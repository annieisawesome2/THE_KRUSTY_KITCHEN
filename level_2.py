
import pygame
from text import Text
from window import Window
from image import ImageSprite



##Fruits on clouds random every time hitting objects


class Level2: 
    def __init__(self):
        self.__WINDOW = Window("Fat Bear")
    
        self.__TITLE = Text("Fat Bear")
        self.__TITLE.setPosition((self.__WINDOW.getWidth()//2 - self.__TITLE.getWidth()//2, 0))
        self.__TITLE.setColor((0, 0, 102))
        self.__TITLE.setFontSize(50)
      

        self.__BG_IMAGE = ImageSprite("images/night_bg.jpeg")
        self.__BG_IMAGE.setScale(4)
        self.__BG_IMAGE.setPosition((0, self.__TITLE.getHeight()))

        self.BELT = [ImageSprite("level2_images/animated1.png"),
                    ImageSprite("level2_images/animated2.png"),
                    ImageSprite("level2_images/animated3.png"),
                    ImageSprite("level2_images/animated4.png")
            ]
        for belt in self.BELT:
            belt.setScale(0.5)
            belt.setPosition((50, 50))
       


    
    def run(self):
        
        while True:
            # -- INPUTS -- #
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__BG_IMAGE.getSurface(), self.__BG_IMAGE.getPOS())
            self.__WINDOW.getSurface().blit(self.__TITLE.getSurface(), self.__TITLE.getPOS())

            for belt in self.BELT:
                self.__WINDOW.getSurface().blit(belt.getSurface(), belt.getPOS())

      
            self.__WINDOW.updateFrame()


       
    
if __name__ == "__main__":
    pygame.init()
    GAME = Level2()
    GAME.run()