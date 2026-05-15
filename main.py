import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
        
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"{SCREEN_WIDTH}")
    print(f"{SCREEN_HEIGHT}")

    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable) 
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    AsteroidField()
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
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()   
    


if __name__ == "__main__":
    main()
