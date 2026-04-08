import pygame
import constants
from player import Player
from logger import log_state

def main():    
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    #print(f"Starting Asteroids with pygame version: {pygame.version.ver}") 
    #print(f"Screen width: {constants.SCREEN_WIDTH}")
    #print(f"Screen height: {constants.SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    # player object
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    # game loop
    while True:
        log_state()

        # process the pygame event queue
        for event in pygame.event.get():
            if event.type == pygame.quit:
                return

        player.update(dt)
        color = (0, 0, 0)
        screen.fill(color)
        player.draw(screen)
        pygame.display.flip()

        # pause game loop for 1/60th sec
        dt = (clock.tick(60) / 1000)
        #print(dt)

if __name__ == "__main__":
    main()
