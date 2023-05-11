from sprite import MySprite
from window import Window
import pygame

class Text(MySprite):
    ##Text object inheriting from MySprite
    """concrete text sprite
    """
    def __init__(self, TEXT):
        MySprite.__init__(self)
        self.__TEXT = TEXT  ## ENCAPSULATION (protecting and hiding data through an interface)
        self.__FONT = pygame.font.SysFont("Ariel", 36)
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR)
    
    # -- MODIFIER METHODS -- #
    def setColor(self, TUPLE):
        #polymorphs the setColor class from MySprite
        MySprite.setColor(self, TUPLE)
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR) ## rerendering the color

    def setFontSize(self, NEW_SIZE):
        self.__FONT_SIZE = NEW_SIZE
        self.__FONT = pygame.font.SysFont("Ariel", self.__FONT_SIZE)
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR)


    # -- ACCESSOR METHODS -- #

if __name__ == "__main__":
    pygame.init()
    WINDOW = Window("Text Title")
    TEXT = Text("Hello World")
    TEXT.setColor((0, 255, 255))
    TEXT.setSpeed(10)

    while True:
        # -- INPUTS -- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # -- PROCESSING -- #
        TEXT.marqueeY(WINDOW.getWidth())

        # -- OUTPUTS -- #
        WINDOW.clearScreen()
        WINDOW.getSurface().blit(TEXT.getSurface(), TEXT.getPOS())
        WINDOW.updateFrame()






