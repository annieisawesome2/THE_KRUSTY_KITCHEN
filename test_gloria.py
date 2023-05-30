
import pygame
from text import Text
from window import Window
from boxes import Box
from image import ImageSprite
from cannon import Cannon
from ball import Ball
from items import Items
import random


##Fruits on clouds random every time hitting objects


class Level1: 
    def __init__(self):
        self.__WINDOW = Window("Spongebob")

        self.__BALL = Box(15, 15)
        self.__BALL.setSpeed(0)
        self.__BALL.setPosition((self.__WINDOW.getWidth()//2 - self.__BALL.getWidth()//2, 650))

        self.PLAY = False

        self.START_MESSAGE = Text("'ENTER' to play!")
        self.START_MESSAGE.setPosition((self.__WINDOW.getWidth()//2 - self.START_MESSAGE.getWidth()//2, self.__WINDOW.getHeight()//2 - self.START_MESSAGE.getHeight()//2))
        self.DIE_MESSAGE = Text("You lose! 'ENTER' to try again")
        self.DIE_MESSAGE.setPosition((-1000, -1000))
        self.WIN_MESSAGE = Text("You Win! 'ENTER' to play Level 2!")
        self.WIN_MESSAGE.setPosition((-1000, -1000))
        
        self.__BG_IMAGE = ImageSprite("images/krusty_krab_kitchen.jpeg")
        self.__BG_IMAGE.setScale(1.4, 1.6)
        self.__BG_IMAGE.setPosition((self.__WINDOW.getWidth() - self.__BG_IMAGE.getWidth(), 0))

        self.__CANNON = Cannon("images/cannon.png")
        self.__CANNON.setScale(0.16)
        self.__CANNON.setPosition((-60, 200))
        self.__CANNON.setSpeed(15)

        self.__BALLS = []
    
        self.NEXT_BALL = 0
        
        self.NEXT_ITEM = 0
        self.STUFF = []

        self.__BUCKET = ImageSprite("images/bucket.png")
        self.__BUCKET.setPosition((1085, 530))
        self.__BUCKET.setScale(0.2)
        self.__FRONT_BUCKET = ImageSprite("images/bucket2.png")
        self.__FRONT_BUCKET.setPosition((1085, 585))
        self.__FRONT_BUCKET.setScale(0.2)

        self.POINTS = 0
        self.HEALTH_BAR = []
        for i in range(15):
            self.HEALTH_BAR.append(Box(15, 15))
            self.HEALTH_BAR[i].setPosition(
                (
                    self.__WINDOW.getWidth() - 50,
                    self.__WINDOW.getHeight() - 10 - (i+1)*17
                )
            )

        

    def generate(self):
        STRING = ["images/bun1.png", "images/bun2.png", "images/patty.png", "images/pickles.png", "images/lettuce.png", "images/tomatos.png", "images/bacon.png", "images/egg.png", "images/cheese.png", "images/ketchup.png", "images/mustard.png", "images/peppers.png", "images/onions.png", "images/pickles.png"]
        print(len(STRING))
        CHOSEN_ITEM = random.choice(STRING)

        ITEM = Items(CHOSEN_ITEM)
        ITEM.setScale(1.5)

        return ITEM
        

    
    def run(self):
        

        while True:
            # -- INPUTS -- #
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            
            
            
            KEYS_PRESSED = pygame.key.get_pressed()

            if KEYS_PRESSED[pygame.K_RETURN]:
                self.PLAY = True
                pygame.mixer.music.play(-1)

            # -- PROCESSING -- #
            if self.PLAY:
                self.START_MESSAGE.setPosition((-1000, -1000))

                self.__CANNON.moveUpDown(KEYS_PRESSED)
                self.__CANNON.checkBoundaries(-100, 820)

                # items
                TIME = pygame.time.get_ticks()
                if TIME > self.NEXT_ITEM:
                    DELAY = 1500

                    self.NEXT_ITEM = TIME + DELAY
                    ITEM = self.generate()
                    
                    self.STUFF.append(ITEM)
                    ITEM.setScale(0.8)
                    ITEM.setPosition((550, -5 - ITEM.getHeight()))
                    ITEM.setgo()
                
            # balls
            TIME1 = pygame.time.get_ticks()
            if self.PLAY and KEYS_PRESSED[pygame.K_SPACE] and TIME1 > self.NEXT_BALL:
                DELAY_1 = 400
                self.NEXT_BALL = TIME1 + DELAY_1
    
                BALL = Ball("images/ball.png")

                self.__BALLS.append(BALL)
                BALL.setScale(0.03)
                BALL.setPosition((self.__CANNON.getX() + 160, self.__CANNON.getY()+100))
                BALL.setSpeed(25)
                BALL.changeShoot()

            for ball in self.__BALLS:
                if ball.getShoot():
                    ball.marqueeX()
                if ball.getPOS()[0] > self.__WINDOW.getWidth():
                    self.__BALLS.pop(0)
                    del ball

            #-----collisions ----------------
            for ball in self.__BALLS:
                for stuff in self.STUFF:
                    BALL_MASK = pygame.mask.from_surface(ball.getSurface())
                    ITEM_MASK = pygame.mask.from_surface(stuff.getSurface())
                    if BALL_MASK.overlap(ITEM_MASK, ((stuff._X - ball._X, stuff._Y - ball._Y))):
                        pygame.mixer.Sound.play(COLLISION_SOUND)
                        ball.setPosition((-1000,-1000))
                        self.__BALLS.remove(ball)
                        stuff.setPosition((-1000,-1000))
                        self.STUFF.remove(stuff)
             
            for stuff in self.STUFF:
                if ITEM.getGo:
                    stuff.marqueeY(self.__WINDOW.getHeight(), 12)
                
                # points
                if stuff.getCollected():
                    if stuff.getFileLoc() != "images/purple_poison.png" and stuff.getFileLoc() != "images/poison.png" and stuff.getFileLoc() != "images/bomb.png":
                        self.POINTS += 1
                        pygame.mixer.Sound.play(FRUIT_SOUND)
                    elif stuff.getFileLoc() == "images/poison.png":
                        self.POINTS -= 1
                        pygame.mixer.Sound.play(POISON_SOUND)
                    elif stuff.getFileLoc() == "images/purple_poison.png":
                        self.POINTS -= 3
                        pygame.mixer.Sound.play(POISON_SOUND)
                    elif stuff.getFileLoc() == "images/bomb.png":
                        self.POINTS -= 15
                        pygame.mixer.Sound.play(POISON_SOUND)
                    self.STUFF.remove(stuff)
                    del stuff

            # health bar
            if self.POINTS > 0 and self.POINTS <=5:
                for i in range(len(self.HEALTH_BAR)):
                    if i < self.POINTS:
                        self.HEALTH_BAR[i].setColor((255, 0, 0))
                    else:
                        self.HEALTH_BAR[i].setColor((255, 255, 255))
            if self.POINTS > 5 and self.POINTS <=15:
                for i in range(len(self.HEALTH_BAR)):
                    if i < self.POINTS:
                        self.HEALTH_BAR[i].setColor((0, 255, 0))
                    else:
                        self.HEALTH_BAR[i].setColor((255, 255, 255))
            
            # die screen
            if self.POINTS < 0:
                pygame.mixer.music.stop()

                self.PLAY = False
                for stuff in self.STUFF:
                    stuff.setPosition((-1000, -1000))
                self.DIE_MESSAGE.setPosition((self.__WINDOW.getWidth()//2 - self.DIE_MESSAGE.getWidth()//2, self.__WINDOW.getHeight()//2 - self.DIE_MESSAGE.getHeight()//2))
                if KEYS_PRESSED[pygame.K_RETURN]:
                    self.__init__()

            # win screen
            elif self.POINTS >= 15:
                self.PLAY = False
                for stuff in self.STUFF:
                    stuff.setPosition((-1000, -1000))
                self.WIN_MESSAGE.setPosition((self.__WINDOW.getWidth()//2 - self.WIN_MESSAGE.getWidth()//2, self.__WINDOW.getHeight()//2 - self.WIN_MESSAGE.getHeight()//2))
                if KEYS_PRESSED[pygame.K_RETURN]:
                    pass
   
            # -- OUTPUTS -- #
                
            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__BG_IMAGE.getSurface(), self.__BG_IMAGE.getPOS())

            # cannon
            self.__WINDOW.getSurface().blit(self.__CANNON.getSurface(), self.__CANNON.getPOS())

            # bucket
            self.__WINDOW.getSurface().blit(self.__BUCKET.getSurface(), self.__BUCKET.getPOS())
        
            # items
            for stuff in self.STUFF:
                self.__WINDOW.getSurface().blit(stuff.getSurface(), stuff.getPOS())

            # balls
            for ball in self.__BALLS:
                self.__WINDOW.getSurface().blit(ball.getSurface(), ball.getPOS())

            # bucket
            self.__WINDOW.getSurface().blit(self.__FRONT_BUCKET.getSurface(), self.__FRONT_BUCKET.getPOS())

            # health bar
            for interval in self.HEALTH_BAR:
                self.__WINDOW.getSurface().blit(interval.getSurface(), interval.getPOS())

            # text
            self.__WINDOW.getSurface().blit(self.START_MESSAGE.getSurface(), self.START_MESSAGE.getPOS())
            self.__WINDOW.getSurface().blit(self.DIE_MESSAGE.getSurface(), self.DIE_MESSAGE.getPOS())
            self.__WINDOW.getSurface().blit(self.WIN_MESSAGE.getSurface(), self.WIN_MESSAGE.getPOS())

            self.__WINDOW.updateFrame()


if __name__ == "__main__":
    pygame.init()
    pygame.mixer.music.load("sounds/bubble_bath.mp3")
    FRUIT_SOUND = pygame.mixer.Sound("sounds/fruit_sound.mp3")
    POISON_SOUND = pygame.mixer.Sound("sounds/bad_sound.mp3")
    COLLISION_SOUND = pygame.mixer.Sound("sounds/Pop.mp3")
    
    GAME = Level1()
    GAME.run()