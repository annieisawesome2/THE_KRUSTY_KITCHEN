
import pygame
from text import Text
from window import Window
from image import ImageSprite
import random
from items import Items
from cannon import Cannon
from ball import Ball
from boxes import Box


##Fruits on clouds random every time hitting objects


class Level2: 
    def __init__(self):
        self.__WINDOW = Window("Fruit Explosion")
        self.__WINDOW.BG_COLOR = ((255, 255, 255))

        # background
        self.__BG_IMAGE = ImageSprite("images/night_bg.jpeg")
        self.__BG_IMAGE.setScale(3)
        self.__BG_IMAGE.setPosition((0, 0))

        # messages
        self.PLAY = False

        self.START_MESSAGE = Text("'ENTER' to play!")
        self.START_MESSAGE.setPosition((self.__WINDOW.getWidth()//2 - self.START_MESSAGE.getWidth()//2, self.__WINDOW.getHeight()//2 - self.START_MESSAGE.getHeight()//2))
        self.DIE_MESSAGE = Text("You lose! 'ENTER' to try again")
        self.DIE_MESSAGE.setPosition((-1000, -1000))
        self.WIN_MESSAGE = Text("You Win!")
        self.WIN_MESSAGE.setPosition((-1000, -1000))

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

        # items
        self.NEXT_ITEM = 0
        self.BOXES = []
        self.ITEMS = []

        # black hole
        self.HOLE = ImageSprite("images/hole.png")
        self.HOLE.setScale(0.3)
        self.HOLE.setPosition((self.__WINDOW.getWidth() - 95, 290))
        self.FRONT_HOLE = ImageSprite("images/hole2.png")
        self.FRONT_HOLE.setScale(0.3)
        self.FRONT_HOLE.setPosition((self.__WINDOW.getWidth() - 55, 290))

        # health bar
        self.POINTS = 1
        self.HEALTH_BAR = []
        for i in range(15):
            self.HEALTH_BAR.append(Box(15, 15))
            self.HEALTH_BAR[i].setPosition(
                (
                    self.__WINDOW.getWidth() - 30,
                    self.__WINDOW.getHeight() - 10 - (i+1)*17
                )
            )

    def generate(self):
        STRING = ["images/banana.png", "images/cherry.png", "images/pear.png", "images/apple.png", "images/orange.png", "images/poison.png", "images/purple_poison.png", "images/poison.png", "images/purple_poison.png", "images/bomb.png"]
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
        elif CHOSEN_ITEM == "images/bomb.png":
            ITEM.setScale(0.05)

        return ITEM
    
    def run(self):
        
        while True:

            # -- INPUTS -- #
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            KEYS_PRESSED = pygame.key.get_pressed()

            # --- PROCESSING --- #
            if KEYS_PRESSED[pygame.K_RETURN]:
                self.PLAY = True
                pygame.mixer.music.play(-1)

            if self.PLAY:
                self.START_MESSAGE.setPosition((-1000, -1000))

                # shooters ------------------------------------------------------------
                # shooter 1
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

                # shooter 2
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
                    BULLET_MASK1 = pygame.mask.from_surface(bullet.getSurface())
                    BOX_MASK1 = pygame.mask.from_surface(box.getSurface())
                    if BULLET_MASK1.overlap(BOX_MASK1, ((box._X - bullet._X, box._Y - bullet._Y))):
                        NEW_ITEM = self.generate()
                        NEW_ITEM.setPosition((box.getX(), box.getY() )) # y + 30
                        NEW_ITEM.setgo()
                        self.ITEMS.append(NEW_ITEM)
                        if box.getPOS()[1] == 200:
                            NEW_ITEM.setDirX(-1)
                        box.setPosition((-1000,1000))
                        bullet.setPosition((-1000,-1000))
            
            for bullet in self.BULLETS_1:
                for item in self.ITEMS:
                    BULLET_MASK1_I = pygame.mask.from_surface(bullet.getSurface())
                    ITEM_MASK1 = pygame.mask.from_surface(item.getSurface())
                    if BULLET_MASK1_I.overlap(ITEM_MASK1, ((item._X - bullet._X, item._Y - bullet._Y))):
                        item.setPosition((-1000,1000))
                        bullet.setPosition((-1000,-1000))
            
            
            for bullet in self.BULLETS_2:
                for box in self.BOXES:
                    BULLET_MASK2 = pygame.mask.from_surface(bullet.getSurface())
                    BOX_MASK2 = pygame.mask.from_surface(box.getSurface())
                    if BULLET_MASK2.overlap(BOX_MASK2, ((box._X - bullet._X, box._Y - bullet._Y))):
                        NEW_ITEM2 = self.generate()
                        NEW_ITEM2.setPosition((box.getX(), box.getY() )) # y + 30
                        NEW_ITEM2.setgo()
                        self.ITEMS.append(NEW_ITEM2)
                        if box.getPOS()[1] == 200:
                            NEW_ITEM2.setDirX(-1)
                        box.setPosition((-1000,1000))
                        bullet.setPosition((-1000,-1000))

            for bullet in self.BULLETS_2:
                for item in self.ITEMS:
                    BULLET_MASK2_I = pygame.mask.from_surface(bullet.getSurface())
                    ITEM_MASK2 = pygame.mask.from_surface(item.getSurface())
                    if BULLET_MASK2_I.overlap(ITEM_MASK2, ((item._X - bullet._X, item._Y - bullet._Y))):
                        item.setPosition((-1000,1000))
                        bullet.setPosition((-1000,-1000))
                        


            for bullet in self.BULLETS_3:
                for box in self.BOXES:
                    BULLET_MASK3 = pygame.mask.from_surface(bullet.getSurface())
                    BOX_MASK3 = pygame.mask.from_surface(box.getSurface())
                    if BULLET_MASK3.overlap(BOX_MASK3, ((box._X - bullet._X, box._Y - bullet._Y))):
                        NEW_ITEM3 = self.generate()
                        NEW_ITEM3.setPosition((box.getX(), box.getY() )) # y + 30
                        NEW_ITEM3.setgo()
                        self.ITEMS.append(NEW_ITEM3)
                        if box.getPOS()[1] == 200:
                            NEW_ITEM3.setDirX(-1)
                        box.setPosition((-1000,1000))
                        bullet.setPosition((-1000,-1000))
            
            for bullet in self.BULLETS_3:
                for item in self.ITEMS:
                    BULLET_MASK3_I = pygame.mask.from_surface(bullet.getSurface())
                    ITEM_MASK3 = pygame.mask.from_surface(item.getSurface())
                    if BULLET_MASK3_I.overlap(ITEM_MASK3, ((item._X - bullet._X, item._Y - bullet._Y))):
                        item.setPosition((-1000,1000))
                        bullet.setPosition((-1000,-1000))
                        

            for bullet in self.BULLETS_4:
                for box in self.BOXES:
                    BULLET_MASK4 = pygame.mask.from_surface(bullet.getSurface())
                    BOX_MASK4 = pygame.mask.from_surface(box.getSurface())
                    if BULLET_MASK4.overlap(BOX_MASK4, ((box._X - bullet._X, box._Y - bullet._Y))):
                        NEW_ITEM4 = self.generate()
                        NEW_ITEM4.setPosition((box.getX(), box.getY() )) # y + 30
                        NEW_ITEM4.setgo()
                        self.ITEMS.append(NEW_ITEM4)
                        if box.getPOS()[1] == 200:
                            NEW_ITEM4.setDirX(-1)
                        box.setPosition((-1000,1000))
                        bullet.setPosition((-1000,-1000))
            
            for bullet in self.BULLETS_4:
                for item in self.ITEMS:
                    BULLET_MASK4_I = pygame.mask.from_surface(bullet.getSurface())
                    ITEM_MASK4 = pygame.mask.from_surface(item.getSurface())
                    if BULLET_MASK4_I.overlap(ITEM_MASK4, ((item._X - bullet._X, item._Y - bullet._Y))):
                        item.setPosition((-1000,1000))
                        bullet.setPosition((-1000,-1000))
                        

            
      
            
            
            for item in self.ITEMS:
                if item.getGo():
                    if item._Y == 185:
                        item._DIR_X = -1
                        item.marqueeX(self.__WINDOW.getWidth(), 8)
                    else:
                        item.marqueeX(self.__WINDOW.getWidth(), 8)
            

            ##--- Checking for collisions then deleting item.... check for missed objects if it goes off screen without hit
            for item in self.ITEMS:    
                if item._POS == ((-1000, -1000)) or (item._Y == 350 and item._X > self.__WINDOW.getWidth()):
                    self.ITEMS.remove(item)
                    del item

            for box in self.BOXES:
                if box._POS == ((-1000, -1000)) or (box._Y == 350 and box._X > self.__WINDOW.getWidth()):
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
            
            for bullet4 in self.BULLETS_4:
                if bullet4._POS == ((-1000, -1000)) or bullet4._Y < 0 - bullet4.getHeight():
                    self.BULLETS_4.remove(bullet4)
                    del bullet4

            # points
            for item in self.ITEMS:
                if item.getPOS()[0] > self.__WINDOW.getWidth()-20 and item.getPOS()[1] == 350:
                    item.setCollected(True)
                if item.getCollected():
                    if item.getFileLoc() == "images/box.png":
                        pass
                    elif item.getFileLoc() != "images/purple_poison.png" and item.getFileLoc() != "images/poison.png" and item.getFileLoc() != "images/bomb.png":
                        self.POINTS += 1
                        pygame.mixer.Sound.play(FRUIT_SOUND)
                    elif item.getFileLoc() == "images/poison.png":
                        self.POINTS -= 1
                        pygame.mixer.Sound.play(POISON_SOUND)
                    elif item.getFileLoc() == "images/purple_poison.png":
                        self.POINTS -= 3
                        pygame.mixer.Sound.play(POISON_SOUND)
                    elif item.getFileLoc() == "images/bomb.png":
                        self.POINTS -= 15
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
            
            # die screen
            if self.POINTS <= 0:
                self.PLAY = False
                pygame.mixer.music.stop()
                for item in self.ITEMS:
                    item.setPosition((-1000, -1000))
                for box in self.BOXES:
                    box.setPosition((-1000, -1000))
                self.DIE_MESSAGE.setPosition((self.__WINDOW.getWidth()//2 - self.DIE_MESSAGE.getWidth()//2, self.__WINDOW.getHeight()//2 - self.DIE_MESSAGE.getHeight()//2))
                if KEYS_PRESSED[pygame.K_RETURN]:
                    self.__init__()

            # win screen
            elif self.POINTS >= 15:
                self.PLAY = False
                for item in self.ITEMS:
                    item.setPosition((-1000, -1000))
                for box in self.BOXES:
                    box.setPosition((-1000, -1000))
                self.WIN_MESSAGE.setPosition((self.__WINDOW.getWidth()//2 - self.WIN_MESSAGE.getWidth()//2, self.__WINDOW.getHeight()//2 - self.WIN_MESSAGE.getHeight()//2))
                if KEYS_PRESSED[pygame.K_RETURN]:
                    pass
    
            # -- OUTPUTS -- #
            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__BG_IMAGE.getSurface(), self.__BG_IMAGE.getPOS())

            self.__WINDOW.getSurface().blit(self.HOLE.getSurface(), self.HOLE.getPOS())

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

            self.__WINDOW.getSurface().blit(self.FRONT_HOLE.getSurface(), self.FRONT_HOLE.getPOS())
            
            self.__WINDOW.getSurface().blit(self.SHOOTER_1.getSurface(), self.SHOOTER_1.getPOS())
            self.__WINDOW.getSurface().blit(self.SHOOTER_2.getSurface(), self.SHOOTER_2.getPOS())
            self.__WINDOW.getSurface().blit(self.SHOOTER_3.getSurface(), self.SHOOTER_3.getPOS())
            self.__WINDOW.getSurface().blit(self.SHOOTER_4.getSurface(), self.SHOOTER_4.getPOS())

            # health bar
            for interval in self.HEALTH_BAR:
                self.__WINDOW.getSurface().blit(interval.getSurface(), interval.getPOS())
            
            # text
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


    GAME = Level2()
    GAME.run()