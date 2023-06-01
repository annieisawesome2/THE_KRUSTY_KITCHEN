import pygame

from window import Window
from image import ImageSprite

class Engine:
    def __init__(self):
        self.WINDOW = Window("Spongebob")

        self.BG_IMAGE = ImageSprite("images/menu_bg.png")
        self.BG_IMAGE.setScale(0.7, 0.8)
        self.BG_IMAGE.setPosition((0,0))

        self.PLAY_1 = ImageSprite("images/wooden_sign.png")
        self.PLAY_1.setScale(1)
        self.PLAY_1.setPosition((700,50))

        self.KRABBY_CASH = ImageSprite("images/krabby_kash.png")
        self.KRABBY_CASH.setScale(0.47)
        self.KRABBY_CASH.setPosition((720,130))

        self.CRAB = ImageSprite("images/crab.png")
        self.CRAB.setScale(0.2)
        self.CRAB.setPosition((1000,50))



        self.PLAY_2 = ImageSprite("images/wooden_sign.png")
        self.PLAY_2.setScale(1)
        self.PLAY_2.setPosition((380,320))

        self.PERFECT_BURGER = ImageSprite("images/perfect_burger.png")
        self.PERFECT_BURGER.setScale(0.47)
        self.PERFECT_BURGER.setPosition((400,400))
        
        self.BURGER = ImageSprite("images/burger.png")
        self.BURGER.setScale(0.055)
        self.BURGER.setPosition((340,470))

        self.SQUID = ImageSprite("images/squid.png")
        self.SQUID.setScale(0.2)
        

    def run(self):
        while True:
            # -- INPUTS -- #
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("pressed")
                    
                MOUSE_POS = pygame.mouse.get_pos()
                self.SQUID.setPosition((MOUSE_POS[0]-25, MOUSE_POS[1]-20))

                
            self.WINDOW.clearScreen()
            self.WINDOW.getSurface().blit(self.BG_IMAGE.getSurface(), self.BG_IMAGE.getPOS())
            self.WINDOW.getSurface().blit(self.PLAY_1.getSurface(), self.PLAY_1.getPOS())
            self.WINDOW.getSurface().blit(self.PLAY_2.getSurface(), self.PLAY_2.getPOS())
            
            self.WINDOW.getSurface().blit(self.KRABBY_CASH.getSurface(),self.KRABBY_CASH.getPOS())
            self.WINDOW.getSurface().blit(self.PERFECT_BURGER.getSurface(),self.PERFECT_BURGER.getPOS())
            self.WINDOW.getSurface().blit(self.CRAB.getSurface(), self.CRAB.getPOS())
            self.WINDOW.getSurface().blit(self.BURGER.getSurface(), self.BURGER.getPOS())
            self.WINDOW.getSurface().blit(self.SQUID.getSurface(), self.SQUID.getPOS())


            self.WINDOW.updateFrame()


if __name__ == "__main__":
    pygame.init()
   
    
    GAME = Engine()
    GAME.run()