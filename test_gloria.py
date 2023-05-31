
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

        self.PLAYER = Cannon("images/spongebob.png")
        self.PLAYER.setScale(0.25)
        self.PLAYER.setPosition((0, 200))
        self.PLAYER.setSpeed(15)

        self.__BALL = Box(15, 15)
        self.__BALL.setSpeed(0)
        self.__BALL.setPosition((self.__WINDOW.getWidth()//2 - self.__BALL.getWidth()//2, 650))
        self.__BALLS = []
        self.NEXT_BALL = 0

        self.PLATE = ImageSprite("images/plate.png")
        self.PLATE.setScale(1)
        self.PLATE.setPosition((1040, 620))

        # items
        self.IMAGE_LOCS = [ # duplicates to increase probability of including most common ingredients
            "images/bun_top.png", "images/bun_top.png",
            "images/bun_bottom.png", "images/bun_bottom.png",
            "images/patty.png", "images/patty.png",
            "images/lettuce.png",
            "images/cheese.png",
            "images/pickles.png",
            "images/tomatos.png",
            "images/egg.png",
            "images/ketchup.png",
            "images/mustard.png",
        ]

        self.INGREDIENTS = []
        for loc in self.IMAGE_LOCS:
            ITEM = Items(loc)
            if loc == "images/ketchup.png" or loc == "images/mustard.png":
                ITEM.setScale(0.2)
            elif loc == "images/pickles.png":
                ITEM.setScale(0.15)
            elif loc == "images/lettuce.png":
                ITEM.setScale(0.6)
            elif loc == "images/bacon.png":
                ITEM.setScale(1.6)
            else:
                ITEM.setScale(1.2)
            self.INGREDIENTS.append(ITEM)
            
        self.NEXT_ITEM = 0
        self.ITEMS = []

        # burger ordered (bottom to top)
        self.BURGER1 = []
        self.BURGER1.append("images/bun_bottom.png") # bottom bun
        for i in range(4):
            self.BURGER1.append(random.choice(self.IMAGE_LOCS[6:])) # middle ingredients
        self.BURGER1.append("images/bun_top.png") # top bun
        for i in range(len(self.BURGER1)):
            self.BURGER1[i].setPosition((100, self.__WINDOW.getHeight()-i*30))
        print(self.BURGER1) # delete ------------------------------------------------------------------------------------------------------------------------

        # burger built (bottom to top)
        self.BURGER2 = []

        # health bar
        self.POINTS = 0
        self.HEALTH_BAR = []
        for i in range(10):
            self.HEALTH_BAR.append(Box(20, 20))
            self.HEALTH_BAR[i].setPosition(
                (
                    self.__WINDOW.getWidth() - 30,
                    self.__WINDOW.getHeight() - 100 - (i+1)*22
                )
            )
            if i > 5:
                self.HEALTH_BAR[i].setColor((255, 230, 100))

    def generate(self):
        CHOSEN_ITEM = random.choice(self.IMAGE_LOCS)
        ITEM = Items(CHOSEN_ITEM)
        self.ITEMS.append(ITEM)

        return ITEM
        
    def dieScreen(self, PRESSED_KEYS):
        pygame.mixer.music.stop()

        self.PLAY = False
        for item in self.ITEMS:
            item.setPosition((-1000, -1000))
        self.DIE_MESSAGE.setPosition((self.__WINDOW.getWidth()//2 - self.DIE_MESSAGE.getWidth()//2, self.__WINDOW.getHeight()//2 - self.DIE_MESSAGE.getHeight()//2))
        if PRESSED_KEYS[pygame.K_RETURN]:
            self.__init__()

    def winScreen(self, PRESSED_KEYS):
        self.PLAY = False
        for item in self.ITEMS:
            item.setPosition((-1000, -1000))
        self.WIN_MESSAGE.setPosition((self.__WINDOW.getWidth()//2 - self.WIN_MESSAGE.getWidth()//2, self.__WINDOW.getHeight()//2 - self.WIN_MESSAGE.getHeight()//2))
        if PRESSED_KEYS[pygame.K_RETURN]:
            pass
    
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

                self.PLAYER.moveUpDown(KEYS_PRESSED)
                self.PLAYER.checkBoundaries(-100, 820)

                # items
                TIME = pygame.time.get_ticks()
                if TIME > self.NEXT_ITEM:
                    DELAY = 1500

                    self.NEXT_ITEM = TIME + DELAY
                    ITEM = self.generate()
                    
                    self.ITEMS.append(ITEM)
                    ITEM.setPosition((550, -5 - ITEM.getHeight()))
                    ITEM.setGo(True)

            # balls
            TIME1 = pygame.time.get_ticks()
            if self.PLAY and KEYS_PRESSED[pygame.K_SPACE] and TIME1 > self.NEXT_BALL:
                DELAY_1 = 400
                self.NEXT_BALL = TIME1 + DELAY_1
    
                BALL = Ball("images/bubble.png")

                self.__BALLS.append(BALL)
                BALL.setScale(0.03)
                BALL.setPosition((self.PLAYER.getPOS()[0]+160, self.PLAYER.getPOS()[1]+10))
                BALL.setSpeed(25)
                BALL.changeShoot()

            for ball in self.__BALLS:
                if ball.getShoot():
                    ball.marqueeX()
                if ball.getPOS()[0] > self.__WINDOW.getWidth():
                    self.__BALLS.pop(0)
                    del ball

            #----- collisions ----------------
            for ball in self.__BALLS:
                for item in self.ITEMS:
                    BALL_MASK = pygame.mask.from_surface(ball.getSurface())
                    ITEM_MASK = pygame.mask.from_surface(item.getSurface())
                    if BALL_MASK.overlap(ITEM_MASK, ((item._X - ball._X, item._Y - ball._Y))):
                        pygame.mixer.Sound.play(COLLISION_SOUND)
                        ball.setPosition((-1000,-1000))
                        self.__BALLS.remove(ball)
                        item.setPosition((-1000,-1000))
                        self.ITEMS.remove(item)
                        del item

            #----- building burger ----------------
            for item in self.ITEMS:
                if item.getGo():
                    item.marqueeY(self.__WINDOW.getHeight(), 12)

                if self.ITEMS.index(item) < 1:
                    stack_y = 620
                else:
                    previous = self.ITEMS[self.ITEMS.index(item)-1]
                    stack_y = (previous.getPOS()[1] + previous.getHeight()) - 10 - item.getHeight()
                if item.getPOS()[0] == 1100 and item.getPOS()[1] > stack_y:
                    item.setGo(False)
                    item.setCollected(True)
                    self.BURGER2.append(item.getFileLoc())
                    item.setPosition((1100, stack_y))

            # health bar
            for i in range(len(self.BURGER2)):
                if i <= len(self.BURGER1)-1:
                    if self.BURGER2[i] != self.BURGER1[i]:
                        self.HEALTH_BAR[i].setColor((255, 0, 0)) # ingredient doesn't match
                    elif self.BURGER2[i] == self.BURGER1[i]: # ingredient matches in the right spot
                        self.HEALTH_BAR[i].setColor((0, 255, 0))
                else:
                    self.HEALTH_BAR[i].setColor((255, 0, 0))
            
            # die screen
            if len(self.BURGER2) >= 10:
                self.dieScreen(KEYS_PRESSED)

            # win screen
            if self.BURGER2 == self.BURGER1:
                self.winScreen(KEYS_PRESSED)
   
            # -- OUTPUTS -- #
                
            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__BG_IMAGE.getSurface(), self.__BG_IMAGE.getPOS())

            # cannon
            self.__WINDOW.getSurface().blit(self.PLAYER.getSurface(), self.PLAYER.getPOS())

            # plate
            self.__WINDOW.getSurface().blit(self.PLATE.getSurface(), self.PLATE.getPOS())
        
            # items
            for item in self.ITEMS:
                self.__WINDOW.getSurface().blit(item.getSurface(), item.getPOS())

            # balls
            for ball in self.__BALLS:
                self.__WINDOW.getSurface().blit(ball.getSurface(), ball.getPOS())
            
            # burgers
            for item in self.BURGER1:
                self.__WINDOW.getSurface().blit(item.getSurface(), item.getPOS())
            for item in self.BURGER2:
                self.__WINDOW.getSurface().blit(item.getSurface(), item.getPOS())

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
    pygame.mixer.music.load("sounds/level_1_music.mp3")
    FRUIT_SOUND = pygame.mixer.Sound("sounds/fruit_sound.mp3")
    POISON_SOUND = pygame.mixer.Sound("sounds/bad_sound.mp3")
    COLLISION_SOUND = pygame.mixer.Sound("sounds/Pop.mp3")
    
    GAME = Level1()
    GAME.run()