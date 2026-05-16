import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot
        
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"{SCREEN_WIDTH}")
    print(f"{SCREEN_HEIGHT}")

    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable) 
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    AsteroidField()
    Shot.containers = (shots, drawable, updatable)
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    
   

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for aster in asteroids:
            if player.collides_with(aster) == True:
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        for aster in asteroids:
            for shot in shots:
                if shot.collides_with(aster):
                    log_event("asteroid_shot")
                    shot.kill()
                    aster.split()

        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()   
    


if __name__ == "__main__":
    main()
