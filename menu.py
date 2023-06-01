
import pygame

from window import Window
from image import ImageSprite
from level_1 import Level1
from level_2 import Level2 

class Menu:
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

        self.LEVEL_1_RUN = False
        self.LEVEL_2_RUN = False
        

    def run(self):
        while True:
            # -- INPUTS -- #
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    SQUID_MASK = pygame.mask.from_surface(self.SQUID.getSurface())
                    PERFECT_BURGER_MASK = pygame.mask.from_surface(self.PERFECT_BURGER.getSurface())
                    KRABBY_CASH_MASK = pygame.mask.from_surface(self.KRABBY_CASH.getSurface())
                    if SQUID_MASK.overlap(PERFECT_BURGER_MASK, ((self.PERFECT_BURGER._X - self.SQUID._X, self.PERFECT_BURGER._Y - self.SQUID._Y))):
                        pygame.mixer.music.load("sounds/level_1_music.mp3")
                        self.LEVEL_1_RUN = True
                        LEVEL_1 = Level1()
                        LEVEL_1.run()
                        
                        
                    
                    if SQUID_MASK.overlap(KRABBY_CASH_MASK, ((self.KRABBY_CASH._X - self.SQUID._X, self.KRABBY_CASH._Y - self.SQUID._Y))):
                        pygame.mixer.music.load("sounds/bubble_bath.mp3")
                        self.LEVEL_2_RUN = True
                        LEVEL_2 = Level2()
                        LEVEL_2.run()

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


