import pygame
from window import Window
from image import ImageSprite

class Engine:
    def __init__(self):
        self.WINDOW = Window("Spongebob")

        self.BG_IMAGE = ImageSprite("images/menu_bg.png")
        self.BG_IMAGE.setScale(0.7, 0.8)
        self.BG_IMAGE.setPosition((0,0))

        self.PLAY_1 = ImageSprite("images/play_button.png")
        self.PLAY_1.setScale(0.5)
        self.PLAY_1.setPosition((0,500))


    def run(self):
        while True:
            # -- INPUTS -- #
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pass


            
                
            self.WINDOW.clearScreen()
            self.WINDOW.getSurface().blit(self.BG_IMAGE.getSurface(), self.BG_IMAGE.getPOS())
            self.WINDOW.getSurface().blit(self.PLAY_1.getSurface(), self.PLAY_1.getPOS())

            self.WINDOW.updateFrame()


if __name__ == "__main__":
    pygame.init()
   
    
    GAME = Engine()
    GAME.run()