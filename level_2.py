
import pygame
from text import Text
from window import Window
from image import ImageSprite
import random
from items import Items
from cannon import Cannon
from ball import Ball



##Fruits on clouds random every time hitting objects


class Level2: 
    def __init__(self):
        self.__WINDOW = Window("Fat Bear")
        self.__WINDOW.BG_COLOR = ((255, 255, 255))

        # --- SHOOTER 1 -- #
        self.SHOOTER_1 = Cannon("images/shooter.png")
        self.SHOOTER_1.setScale(0.6)
        self.SHOOTER_1.setPosition((170, 680))
    
        self.BULLETS_1 = []
        self.NEXT_BULLET_1 = 0

        # --- SHOOTER 2 -- #
        self.SHOOTER_2 = Cannon("images/shooter.png")
        self.SHOOTER_2.setScale(0.6)
        self.SHOOTER_2.setPosition((445, 680))
        
        self.BULLETS_2 = []
        self.NEXT_BULLET_2 = 0

        # --- SHOOTER 3 -- #
        self.SHOOTER_3 = Cannon("images/shooter.png")
        self.SHOOTER_3.setScale(0.6)
        self.SHOOTER_3.setPosition((715, 680))
        
        self.BULLETS_3 = []
        self.NEXT_BULLET_3 = 0

        # --- SHOOTER 4 -- #
        self.SHOOTER_4 = Cannon("images/shooter.png")
        self.SHOOTER_4.setScale(0.6)
        self.SHOOTER_4.setPosition((983, 680))
        
        self.BULLETS_4 = []
        self.NEXT_BULLET_4 = 0

       
      

        self.__BG_IMAGE = ImageSprite("images/level_2BG.jpg")
        self.__BG_IMAGE.setScale(3)
        self.__BG_IMAGE.setPosition((50, 0))
    

        self.NEXT_ITEM = 0
        self.BOXES = []
        self.ITEMS = []

    def generate(self):
        STRING = ["images/banana.png", "images/cherry.png", "images/pear.png", "images/apple.png", "images/orange.png", "images/poison.png", "images/purple_poison.png", "images/poison.png", "images/purple_poison.png"]
        CHOSEN_ITEM = random.choice(STRING)

        ITEM = Items(CHOSEN_ITEM)

        if CHOSEN_ITEM == "images/banana.png":
            ITEM.setScale(0.04)
        elif CHOSEN_ITEM == "images/cherry.png":
            ITEM.setScale(0.03)
        elif CHOSEN_ITEM == "images/pear.png":
            ITEM.setScale(0.04)
        elif CHOSEN_ITEM == "images/apple.png":
            ITEM.setScale(0.03)
        elif CHOSEN_ITEM == "images/orange.png":
            ITEM.setScale(0.04)
        elif CHOSEN_ITEM == "images/poison.png":
            ITEM.setScale(0.025)
        elif CHOSEN_ITEM == "images/purple_poison.png":
            ITEM.setScale(0.053)

        return ITEM
     


    
    def run(self):
        
        while True:
            # -- INPUTS -- #
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            KEYS_PRESSED = pygame.key.get_pressed()

            # --- SHOOTER 1 -- #
            TIME1 = pygame.time.get_ticks()
            if KEYS_PRESSED[pygame.K_c] and TIME1 > self.NEXT_BULLET_1:
                DELAY_1 = 400
                self.NEXT_BULLET_1 = TIME1 + DELAY_1
       
                BULLET_1 = Ball("images/bullet.png")
                self.BULLETS_1.append(BULLET_1)
                BULLET_1.setScale(0.04)
                BULLET_1.setPosition((self.SHOOTER_1.getX() +60, self.SHOOTER_1.getY()))
                BULLET_1.setSpeed(25)
                BULLET_1.changeShoot()

            for bullet in self.BULLETS_1:
                if bullet.getShoot():
                    bullet.marqueeY()
                if bullet.getPOS()[0] > self.__WINDOW.getWidth(): ###change to height????
                    self.BULLETS_1.pop(0)
                    del bullet

            # --- SHOOTER 2 -- #
            TIME2 = pygame.time.get_ticks()
            if KEYS_PRESSED[pygame.K_v] and TIME2 > self.NEXT_BULLET_2:
                DELAY_2 = 400
                self.NEXT_BULLET_2 = TIME2 + DELAY_2
       
                BULLET_2 = Ball("images/bullet.png")
                self.BULLETS_2.append(BULLET_2)
                BULLET_2.setScale(0.04)
                BULLET_2.setPosition((self.SHOOTER_2.getX() +60, self.SHOOTER_2.getY()))
                BULLET_2.setSpeed(25)
                BULLET_2.changeShoot()

            for bullet in self.BULLETS_2:
                if bullet.getShoot():
                    bullet.marqueeY()
                if bullet.getPOS()[0] > self.__WINDOW.getWidth(): ###change to height????
                    self.BULLETS_2.pop(0)
                    del bullet

            # --- SHOOTER 3 -- #
            TIME3 = pygame.time.get_ticks()
            if KEYS_PRESSED[pygame.K_b] and TIME3 > self.NEXT_BULLET_3:
                DELAY_3 = 400
                self.NEXT_BULLET_3 = TIME3 + DELAY_3
       
                BULLET_3 = Ball("images/bullet.png")
                self.BULLETS_3.append(BULLET_3)
                BULLET_3.setScale(0.04)
                BULLET_3.setPosition((self.SHOOTER_3.getX() +60, self.SHOOTER_3.getY()))
                BULLET_3.setSpeed(25)
                BULLET_3.changeShoot()

            for bullet in self.BULLETS_3:
                if bullet.getShoot():
                    bullet.marqueeY()
                if bullet.getPOS()[0] > self.__WINDOW.getWidth(): ###change to height????
                    self.BULLETS_3.pop(0)
                    del bullet
            
            # --- SHOOTER 4 -- #
            TIME4 = pygame.time.get_ticks()
            if KEYS_PRESSED[pygame.K_n] and TIME4 > self.NEXT_BULLET_4:
                DELAY_4 = 400
                self.NEXT_BULLET_4 = TIME4 + DELAY_4
       
                BULLET_4 = Ball("images/bullet.png")
                self.BULLETS_4.append(BULLET_4)
                BULLET_4.setScale(0.04)
                BULLET_4.setPosition((self.SHOOTER_4.getX() +60, self.SHOOTER_4.getY()))
                BULLET_4.setSpeed(25)
                BULLET_4.changeShoot()

            for bullet in self.BULLETS_4:
                if bullet.getShoot():
                    bullet.marqueeY()
                if bullet.getPOS()[0] > self.__WINDOW.getWidth(): ###change to height????
                    self.BULLETS_4.pop(0)
                    del bullet



            TIME = pygame.time.get_ticks()
            if TIME > self.NEXT_ITEM:
                DELAY = 2000

                self.NEXT_ITEM = TIME + DELAY
                ITEM = Items("images/box.png")
                
                
                self.BOXES.append(ITEM)
                ITEM.setScale(0.1)
                ITEM.setPosition((-5 - ITEM.getWidth(),50))
                ITEM.setgo()
             
            for box in self.BOXES:
                if ITEM.getGo:
                    box.marqueeX(self.__WINDOW.getWidth(), 8)

     
            for bullet in self.BULLETS_1:
                for box in self.BOXES:
                    BULLET_MASK = pygame.mask.from_surface(bullet.getSurface())
                    BOX_MASK = pygame.mask.from_surface(box.getSurface())
                    if BULLET_MASK.overlap(BOX_MASK, ((box._X - bullet._X, box._Y - bullet._Y))):
                        ITEM = self.generate()
                        self.ITEMS.append(ITEM)
                        box = ITEM
                        bullet.setPosition((-1000,-1000))

                        
            for bullet in self.BULLETS_2:
                for box in self.BOXES:
                    BULLET_MASK = pygame.mask.from_surface(bullet.getSurface())
                    BOX_MASK = pygame.mask.from_surface(box.getSurface())
                    if BULLET_MASK.overlap(BOX_MASK, ((box._X - bullet._X, box._Y - bullet._Y))):
                        bullet.setPosition((-1000,-1000))
                        box.setPosition((-1000,-1000))

            for bullet in self.BULLETS_3:
                for box in self.BOXES:
                    BULLET_MASK = pygame.mask.from_surface(bullet.getSurface())
                    BOX_MASK = pygame.mask.from_surface(box.getSurface())
                    if BULLET_MASK.overlap(BOX_MASK, ((box._X - bullet._X, box._Y - bullet._Y))):
                        bullet.setPosition((-1000,-1000))
                        box.setPosition((-1000,-1000))

            for bullet in self.BULLETS_4:
                for box in self.BOXES:
                    BULLET_MASK = pygame.mask.from_surface(bullet.getSurface())
                    BOX_MASK = pygame.mask.from_surface(box.getSurface())
                    if BULLET_MASK.overlap(BOX_MASK, ((box._X - bullet._X, box._Y - bullet._Y))):
                        bullet.setPosition((-1000,-1000))
                        box.setPosition((-1000,-1000))




            
            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__BG_IMAGE.getSurface(), self.__BG_IMAGE.getPOS())
      
            for box in self.BOXES:
                self.__WINDOW.getSurface().blit(box.getSurface(), box.getPOS())

                 

            for bullet in self.BULLETS_1:
                self.__WINDOW.getSurface().blit(bullet.getSurface(), bullet.getPOS())
            
            for bullet in self.BULLETS_2:
                self.__WINDOW.getSurface().blit(bullet.getSurface(), bullet.getPOS())
            
            for bullet in self.BULLETS_3:
                self.__WINDOW.getSurface().blit(bullet.getSurface(), bullet.getPOS())
                
            for bullet in self.BULLETS_4:
                self.__WINDOW.getSurface().blit(bullet.getSurface(), bullet.getPOS())
             
            for item in self.ITEMS:
                self.__WINDOW.getSurface().blit(item.getSurface(), item.getPOS())
            
            self.__WINDOW.getSurface().blit(self.SHOOTER_1.getSurface(), self.SHOOTER_1.getPOS())
            self.__WINDOW.getSurface().blit(self.SHOOTER_2.getSurface(), self.SHOOTER_2.getPOS())
            self.__WINDOW.getSurface().blit(self.SHOOTER_3.getSurface(), self.SHOOTER_3.getPOS())
            self.__WINDOW.getSurface().blit(self.SHOOTER_4.getSurface(), self.SHOOTER_4.getPOS())
            
      
            self.__WINDOW.updateFrame()


       
    
if __name__ == "__main__":
    pygame.init()
    GAME = Level2()
    GAME.run()