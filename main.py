import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state 
        
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"{SCREEN_WIDTH}")
    print(f"{SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()
    dt = 0

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()   

if __name__ == "__main__":
    main()
