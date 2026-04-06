import pygame
import constants
from logger import log_state

def main():    
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    #print(f"Starting Asteroids with pygame version: {pygame.version.ver}") 
    #print(f"Screen width: {constants.SCREEN_WIDTH}")
    #print(f"Screen height: {constants.SCREEN_HEIGHT}")

    while True:
        log_state()

        # process the pygame event queue
        for event in pygame.event.get():
            pass

        color = (0, 0, 0)
        screen.fill(color)
        pygame.display.flip()

if __name__ == "__main__":
    main()
