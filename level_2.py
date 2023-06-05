
import pygame
from text import Text
from window import Window
from image import ImageSprite
import random
from items import Items
from cannon import Cannon
from ball import Ball
from boxes import Box

class Level2: 
    def __init__(self):
        self.__WINDOW = Window("Krabby Kash")
        self.__WINDOW.BG_COLOR = ((255, 255, 255))

        # background
        self.__BG_IMAGE = ImageSprite("images/sand_bg.png")
        self.__BG_IMAGE.setScale(1.4)
        self.__BG_IMAGE.setPosition((0, -100))

        # messages
        self.PLAY = False

        self.START = ImageSprite("images/level2_instructions.png")
        self.START.setScale(0.818)
        # lose
        self.ANGRY_MRKRABS = ImageSprite("images/angry_mrkrabs.png")
        self.ANGRY_MRKRABS.setScale(0.3)
        self.ANGRY_MRKRABS.setPosition((-1000, -1000))
        self.LOSE_MESSAGE = ImageSprite("images/lose_message.png")
        self.LOSE_MESSAGE.setScale(0.8)
        self.LOSE_MESSAGE.setPosition((-1000, -1000))
        # win
        self.HAPPY_MRKRABS = ImageSprite("images/happy_mrkrabs.png")
        self.HAPPY_MRKRABS.setScale(0.5)
        self.HAPPY_MRKRABS.setPosition((-1000, -1000))
        self.WIN_MESSAGE = ImageSprite("images/win_message.png")
        self.WIN_MESSAGE.setScale(0.8)
        self.WIN_MESSAGE.setPosition((-1000, -1000))

        # --- SHOOTER 1 -- #
        self.SHOOTER_1 = Cannon("images/coral_1.png")
        self.SHOOTER_1.setScale(0.9)
        self.SHOOTER_1.setPosition((170, 680))
    
        self.BULLETS_1 = []
        self.NEXT_BULLET_1 = 0

        # --- SHOOTER 2 -- #
        self.SHOOTER_2 = Cannon("images/coral_2.png")
        self.SHOOTER_2.setScale(0.9)
        self.SHOOTER_2.setPosition((445, 660))
        
        self.BULLETS_2 = []
        self.NEXT_BULLET_2 = 0

        # --- SHOOTER 3 -- #
        self.SHOOTER_3 = Cannon("images/coral_3.png")
        self.SHOOTER_3.setScale(0.9)
        self.SHOOTER_3.setPosition((715, 670))
        
        self.BULLETS_3 = []
        self.NEXT_BULLET_3 = 0

        # items
        self.NEXT_ITEM = 0
        self.BOXES = []
        self.ITEMS = []

        # crab and treasure box
        self.RESTAURANT = ImageSprite("images/restaurant.png")
        self.RESTAURANT.setScale(0.3)
        self.RESTAURANT.setPosition((self.__WINDOW.getWidth() - self.RESTAURANT.getWidth(), 380))
        self.RESTAURANT2 = ImageSprite("images/restaurant2.png")
        self.RESTAURANT2.setScale(0.3)
        self.RESTAURANT2.setPosition((self.__WINDOW.getWidth() - self.RESTAURANT.getWidth(), 380))
        self.CRAB = ImageSprite("images/crab.png")
        self.CRAB.setScale(0.2)
        self.CRAB.setPosition((1100, 450))
      
        # health bar
        self.POINTS = 1
        self.HEALTH_BAR = []
        for i in range(15):
            self.HEALTH_BAR.append(Box(20, 20))
            self.HEALTH_BAR[i].setPosition((920 + (i+1)*22, 640))

    def generate(self):
        """Generate cash or plankton

        Returns:
            _type_: _description_
        """
        STRING = ["images/dollar_bill.png", "images/plankton.png"]
        CHOSEN_ITEM = random.choice(STRING)
        ITEM = Items(CHOSEN_ITEM)

        if CHOSEN_ITEM == "images/dollar_bill.png":
            ITEM.setScale(0.21)
        elif CHOSEN_ITEM == "images/plankton.png":
            ITEM.setScale(0.25)
        return ITEM
    
    def run(self):
        
        while True:
            # -- INPUTS -- #
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            FRUIT_SOUND = pygame.mixer.Sound("sounds/money.mp3")
            POISON_SOUND = pygame.mixer.Sound("sounds/bad_sound.mp3")
            COLLISION_SOUND = pygame.mixer.Sound("sounds/bubble_pop.mp3")
            KEYS_PRESSED = pygame.key.get_pressed()

            # --- PROCESSING --- #
            if KEYS_PRESSED[pygame.K_RETURN]:
                self.PLAY = True
                pygame.mixer.music.play(-1)

            if self.PLAY:
                self.START.setPosition((-2000, -1000))

                # ----- shooter 1 ----- #
                TIME1 = pygame.time.get_ticks()
                if KEYS_PRESSED[pygame.K_a] and TIME1 > self.NEXT_BULLET_1:
                    DELAY_1 = 400
                    self.NEXT_BULLET_1 = TIME1 + DELAY_1
        
                    BULLET_1 = Ball("images/squid.png")
                    self.BULLETS_1.append(BULLET_1)
                    BULLET_1.setScale(0.15)
                    BULLET_1.setPosition((self.SHOOTER_1.getPOS()[0] +50, self.SHOOTER_1.getPOS()[1] +60))
                    BULLET_1.setSpeed(25)
                    BULLET_1.changeShoot()

                for bullet in self.BULLETS_1:
                    if bullet.getShoot():
                        bullet.marqueeY()
                

                # ----- shooter 2 ----- #
                TIME2 = pygame.time.get_ticks()
                if KEYS_PRESSED[pygame.K_s] and TIME2 > self.NEXT_BULLET_2:
                    DELAY_2 = 400
                    self.NEXT_BULLET_2 = TIME2 + DELAY_2
        
                    BULLET_2 = Ball("images/squid.png")
                    self.BULLETS_2.append(BULLET_2)
                    BULLET_2.setScale(0.15)
                    BULLET_2.setPosition((self.SHOOTER_2.getPOS()[0] +60, self.SHOOTER_2.getPOS()[1]+60))
                    BULLET_2.setSpeed(25)
                    BULLET_2.changeShoot()

                for bullet in self.BULLETS_2:
                    if bullet.getShoot():
                        bullet.marqueeY()
                 

               # ----- shooter 3 ----- #
                TIME3 = pygame.time.get_ticks()
                if KEYS_PRESSED[pygame.K_d] and TIME3 > self.NEXT_BULLET_3:
                    DELAY_3 = 400
                    self.NEXT_BULLET_3 = TIME3 + DELAY_3
        
                    BULLET_3 = Ball("images/squid.png")
                    self.BULLETS_3.append(BULLET_3)
                    BULLET_3.setScale(0.15)
                    BULLET_3.setPosition((self.SHOOTER_3.getPOS()[0] +35, self.SHOOTER_3.getPOS()[1]+60))
                    BULLET_3.setSpeed(25)
                    BULLET_3.changeShoot()

                for bullet in self.BULLETS_3:
                    if bullet.getShoot():
                        bullet.marqueeY()
              
                # --- BUBBLE GENERATOR --- #
                TIME = pygame.time.get_ticks()
                if TIME > self.NEXT_ITEM:
                    DELAY = 1500
                    self.NEXT_ITEM = TIME + DELAY
                    ITEM = Items("images/bubble.png")
                    self.BOXES.append(ITEM)
                    ITEM.setScale(0.07)
                    ITEM.setPosition((-5 - ITEM.getWidth(),50))
                    ITEM.setGo(True)
                
                for box in self.BOXES:
                    if ITEM.getGo:
                        box.marqueeX(self.__WINDOW.getWidth(), 12)

            ## --- COLLISION 1 --- ##
            for bullet in self.BULLETS_1:
                for box in self.BOXES:
                    BULLET_MASK1 = pygame.mask.from_surface(bullet.getSurface())
                    BOX_MASK1 = pygame.mask.from_surface(box.getSurface())
                    if BULLET_MASK1.overlap(BOX_MASK1, ((box._X - bullet._X, box._Y - bullet._Y))):
                        pygame.mixer.Sound.play(COLLISION_SOUND)
                        NEW_ITEM = self.generate()
                        NEW_ITEM.setPosition((box.getPOS()[0], box.getPOS()[1])) # y + 30
                        NEW_ITEM.setGo(True)
                        self.ITEMS.append(NEW_ITEM)
                        if box.getPOS()[1] == 250:
                            NEW_ITEM.setDirX(-1)
                        box.setGo(False)
                        box.setPosition((-1000,-1000))
                        bullet.setPosition((-1000,-1000))
            
            for bullet in self.BULLETS_1:
                for item in self.ITEMS:
                    BULLET_MASK1_I = pygame.mask.from_surface(bullet.getSurface())
                    ITEM_MASK1 = pygame.mask.from_surface(item.getSurface())
                    if BULLET_MASK1_I.overlap(ITEM_MASK1, ((item._X - bullet._X, item._Y - bullet._Y))):
                        item.setGo(False)
                        item.setPosition((-1000,-1000))
                        bullet.setPosition((-1000,-1000))
                        
            
             ## --- COLLISION 2 --- ##
            for bullet in self.BULLETS_2:
                for box in self.BOXES:
                    BULLET_MASK2 = pygame.mask.from_surface(bullet.getSurface())
                    BOX_MASK2 = pygame.mask.from_surface(box.getSurface())
                    if BULLET_MASK2.overlap(BOX_MASK2, ((box._X - bullet._X, box._Y - bullet._Y))):
                        pygame.mixer.Sound.play(COLLISION_SOUND)
                        NEW_ITEM2 = self.generate()
                        NEW_ITEM2.setPosition((box.getPOS()[0], box.getPOS()[1])) # y + 30
                        NEW_ITEM2.setGo(True)
                        self.ITEMS.append(NEW_ITEM2)
                        if box.getPOS()[1] == 250:
                            NEW_ITEM2.setDirX(-1)
                        box.setGo(False)
                        box.setPosition((-1000,-1000))
                        bullet.setPosition((-1000,-1000))

            for bullet in self.BULLETS_2:
                for item in self.ITEMS:
                    BULLET_MASK2_I = pygame.mask.from_surface(bullet.getSurface())
                    ITEM_MASK2 = pygame.mask.from_surface(item.getSurface())
                    if BULLET_MASK2_I.overlap(ITEM_MASK2, ((item._X - bullet._X, item._Y - bullet._Y))):
                        item.setGo(False)
                        item.setPosition((-1000,-1000))
                        bullet.setPosition((-1000,-1000))
                        

             ## --- COLLISION 3 --- ##
            for bullet in self.BULLETS_3:
                for box in self.BOXES:
                    BULLET_MASK3 = pygame.mask.from_surface(bullet.getSurface())
                    BOX_MASK3 = pygame.mask.from_surface(box.getSurface())
                    if BULLET_MASK3.overlap(BOX_MASK3, ((box._X - bullet._X, box._Y - bullet._Y))):
                        pygame.mixer.Sound.play(COLLISION_SOUND)
                        NEW_ITEM3 = self.generate()
                        NEW_ITEM3.setPosition((box.getPOS()[0], box.getPOS()[1] )) # y + 30
                        NEW_ITEM3.setGo(True)
                        self.ITEMS.append(NEW_ITEM3)
                        if box.getPOS()[1] == 250:
                            NEW_ITEM3.setDirX(-1)
                        box.setGo(False)
                        box.setPosition((-1000,-1000))
                        bullet.setPosition((-1000,-1000))
            
            for bullet in self.BULLETS_3:
                for item in self.ITEMS:
                    BULLET_MASK3_I = pygame.mask.from_surface(bullet.getSurface())
                    ITEM_MASK3 = pygame.mask.from_surface(item.getSurface())
                    if BULLET_MASK3_I.overlap(ITEM_MASK3, ((item._X - bullet._X, item._Y - bullet._Y))):
                        item.setGo(False)
                        item.setPosition((-1000,-1000))
                        bullet.setPosition((-1000,-1000))
                
            for item in self.ITEMS:
                if item.getGo():
                    if item._Y == 250:
                        item._DIR_X = -1
                        item.marqueeX(self.__WINDOW.getWidth(), 12)
                    else:
                        item.marqueeX(self.__WINDOW.getWidth(), 12)
                        
             ## --- TREASURE and ITEM COLLSION --- ##
            for item in self.ITEMS:
                if item.getPOS()[0] > 1050 and item.getPOS()[1] == 470:
                    item.setGo(False)
                    item.setPosition((-1000,-1000))
                    item.setCollected(True)
                    
            for box in self.BOXES:
                BOX_MASK = pygame.mask.from_surface(box.getSurface())
                TREASURE_MASK = pygame.mask.from_surface(self.RESTAURANT.getSurface())
                if TREASURE_MASK.overlap(BOX_MASK, ((box._X - self.RESTAURANT._X, box._Y - self.RESTAURANT._Y))):
                    box.setGo(False)
                    box.setPosition((-1000,-1000))
            # points
            for item in self.ITEMS:
                if item.getCollected():
                    if item.getFileLoc() != "images/plankton.png":
                        self.POINTS += 1
                        pygame.mixer.Sound.play(FRUIT_SOUND)
                    elif item.getFileLoc() == "images/plankton.png":
                        self.POINTS -= 3
                        pygame.mixer.Sound.play(POISON_SOUND)
                    self.ITEMS.remove(item)
                    del item

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
            
                    
            
        
            ##--- Checking for collisions then deleting item.... check for missed objects if it goes off screen without hit
            for item in self.ITEMS: 
                if item._X == -1000 and item._Y == -1000:
                    self.ITEMS.remove(item)
                    del item
        

            for box in self.BOXES:
                if box._X == -1000 and box._Y == -1000:
                    self.BOXES.remove(box)
                    del box

           
            
            for bullet1 in self.BULLETS_1:
                if bullet1._POS == ((-1000, -1000)) or bullet1._Y < 0 - bullet1.getHeight() :
                    self.BULLETS_1.remove(bullet1)
                    del bullet1
            
            
            for bullet2 in self.BULLETS_2:
                if bullet2._POS == ((-1000, -1000)) or bullet2._Y < 0 - bullet2.getHeight():
                    self.BULLETS_2.remove(bullet2)
                    del bullet2
            
            for bullet3 in self.BULLETS_3 :
                if bullet3._POS == ((-1000, -1000)) or bullet3._Y < 0 - bullet3.getHeight():
                    self.BULLETS_3.remove(bullet3)
                    del bullet3

            # die screen
            if self.POINTS <= 0:
                self.PLAY = False
                for health in self.HEALTH_BAR:
                    health.setColor((255, 255, 255))
                for item in self.ITEMS:
                    item.setPosition((-1000, -1000))
                for box in self.BOXES:
                    box.setPosition((-1000, -1000))
                self.CRAB.setPosition((-1000, -1000))
                self.ANGRY_MRKRABS.setPosition((1120, 450))
                self.LOSE_MESSAGE.setPosition((self.__WINDOW.getWidth()//2 - self.LOSE_MESSAGE.getWidth()//2, self.__WINDOW.getHeight()//2 - self.LOSE_MESSAGE.getHeight()//2))
                pygame.mixer.music.stop()
                if KEYS_PRESSED[pygame.K_RETURN]:
                    break

            # win screen
            elif self.POINTS >= 15:
                self.PLAY = False
                for item in self.ITEMS:
                    item.setPosition((-1000, -1000))
                for box in self.BOXES:
                    box.setPosition((-1000, -1000))
                self.CRAB.setPosition((-1000, -1000))
                self.HAPPY_MRKRABS.setPosition((1040, 400))
                self.WIN_MESSAGE.setPosition((self.__WINDOW.getWidth()//2 - self.WIN_MESSAGE.getWidth()//2, self.__WINDOW.getHeight()//2 - self.WIN_MESSAGE.getHeight()//2))
                pygame.mixer.music.stop()
                if KEYS_PRESSED[pygame.K_RETURN]:
                    break
    
            # -- OUTPUTS -- #
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
           
            
            self.__WINDOW.getSurface().blit(self.RESTAURANT.getSurface(), self.RESTAURANT.getPOS())
            for item in self.ITEMS:
                self.__WINDOW.getSurface().blit(item.getSurface(), item.getPOS())
            self.__WINDOW.getSurface().blit(self.RESTAURANT2.getSurface(), self.RESTAURANT2.getPOS())
            self.__WINDOW.getSurface().blit(self.CRAB.getSurface(), self.CRAB.getPOS())

            self.__WINDOW.getSurface().blit(self.SHOOTER_1.getSurface(), self.SHOOTER_1.getPOS())
            self.__WINDOW.getSurface().blit(self.SHOOTER_2.getSurface(), self.SHOOTER_2.getPOS())
            self.__WINDOW.getSurface().blit(self.SHOOTER_3.getSurface(), self.SHOOTER_3.getPOS())
      

            # health bar
            for interval in self.HEALTH_BAR:
                self.__WINDOW.getSurface().blit(interval.getSurface(), interval.getPOS())
            
            # start/lose/win
            self.__WINDOW.getSurface().blit(self.START.getSurface(), self.START.getPOS())
            self.__WINDOW.getSurface().blit(self.ANGRY_MRKRABS.getSurface(), self.ANGRY_MRKRABS.getPOS())
            self.__WINDOW.getSurface().blit(self.LOSE_MESSAGE.getSurface(), self.LOSE_MESSAGE.getPOS())
            self.__WINDOW.getSurface().blit(self.HAPPY_MRKRABS.getSurface(), self.HAPPY_MRKRABS.getPOS())
            self.__WINDOW.getSurface().blit(self.WIN_MESSAGE.getSurface(), self.WIN_MESSAGE.getPOS())
      
            self.__WINDOW.updateFrame()


       
if __name__ == "__main__":
    pygame.init()
    pygame.mixer.music.load("sounds/bubble_bath.mp3")
    
    GAME = Level2()
    GAME.run()