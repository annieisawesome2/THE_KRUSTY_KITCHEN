from sprite import MySprite
import pygame

################ gloria edit

class Bucket(MySprite):
    def __init__(self, IMAGE_FILE):
        MySprite.__init__(self)
        self.__FILE_LOC = IMAGE_FILE  ## ENCAPSULATION (protecting and hiding data through an interface)
        self._SURFACE = pygame.image.load(self.__FILE_LOC).convert_alpha()
        # self.HEALTH_BAR = []
        # for i in range(15):
        #     self.HEALTH_BAR.append(MySprite(20, 15))
