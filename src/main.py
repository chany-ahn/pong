import sys, pygame
from ball import Ball
# from paddle import Paddle

def main():
    pygame.init()
    size = width, height = 640, 480
    speed = [2,2]
    black = 0,0,0

    screen = pygame.display.set_mode(size)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            
        screen.fill(black)
        pygame.display.flip()

        pygame.time.delay(3)

if __name__ == "__main__":
    main()