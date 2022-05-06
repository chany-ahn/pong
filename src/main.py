import sys, pygame
from ball import Ball
from game import Game
# from paddle import Paddle

def main():
    pygame.init()
    size = width, height = 640, 480
    black = 0,0,0

    screen = pygame.display.set_mode(size)

    g = Game(width, height)
    g.reset_game()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.fill(black)
        pygame.draw.circle(screen, (255,255,255), g.ball.get_position(), g.ball.r)
        pygame.display.flip()
        pygame.time.delay(3)
        g.update()

if __name__ == "__main__":
    main()