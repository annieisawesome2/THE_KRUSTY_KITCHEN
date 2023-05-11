import pygame

class Window:
    """Create the window that will load pygame
    """
    def __init__(self, TITLE, WIDTH = 1300, HEIGHT=800, FPS=30, BG_COLOR = (102, 0, 102)):
        ## ENCAPSULATION (protecting and hiding data through an interface)
        self.__TITLE = TITLE
        self.__FPS = FPS #frames per second the window will refresh
        self.__WIDTH = WIDTH #width of the window
        self.__HEIGHT = HEIGHT #height of the window
        self.__SCREEN_DIM = (self.__WIDTH, self.__HEIGHT) #screen dimention
        self.__BG_COLOR = BG_COLOR #uses the format (R, G, B)
        self.__FRAME = pygame.time.Clock()
        self.__SURFACE = pygame.display.set_mode(self.__SCREEN_DIM) #surface object in pygame. Every item in your program will overlay on top of a surface object
        self.__SURFACE.fill(self.__BG_COLOR)
        pygame.display.set_caption(self.__TITLE) 

    # -- MODIFIER METHODS -- #
    def updateFrame(self):  
        """updating the window object based on the FPS that we have set
        """
        self.__FRAME.tick(self.__FPS) #waits for the appropriate time based on the set FPS
        pygame.display.flip() #updates the window with the new frame
    
    def clearScreen(self):
        """fill the screen with the background color
        """
        self.__SURFACE.fill(self.__BG_COLOR)

    # -- ACCESSOR METHODS -- #
    def getSurface(self):
        return self.__SURFACE
    
    def getWidth(self):
        return self.__WIDTH
    
    def getHeight(self):
        return self.__HEIGHT

if __name__ == "__main__":
    # main program code
    pygame.init()

    WINDOW = Window("template", 800, 600, 30)
    

    while True:
        # -- INPUTS -- #
        # Allow the x in the title bar to work 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
        # -- OUTPUTS -- #   
        WINDOW.updateFrame() #like the sync function so do it at the end
