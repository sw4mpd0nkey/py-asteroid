import sys
import pygame
import constants
from player import Player
from logger import log_state, log_event
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():    
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    #print(f"Starting Asteroids with pygame version: {pygame.version.ver}") 
    #print(f"Screen width: {constants.SCREEN_WIDTH}")
    #print(f"Screen height: {constants.SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    #group defs
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, drawable, updatable)

    # player object
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    astroid_field = AsteroidField()

    # game loop
    while True:
        log_state()

        # process the pygame event queue
        for event in pygame.event.get():
            if event.type == pygame.quit:
                return

        updatable.update(dt)

        # player collision detection with astroids
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()


        # collision detection for astroid and shots
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.kill()



        # drawing screen
        color = (0, 0, 0)
        screen.fill(color)
        
        for to_draw in drawable:
            to_draw.draw(screen)

        pygame.display.flip()

        # pause game loop for 1/60th sec
        dt = (clock.tick(60) / 1000)
        #print(dt)

if __name__ == "__main__":
    main()
