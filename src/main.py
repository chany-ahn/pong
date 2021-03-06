import sys, pygame
from ball import Ball
from game import Game
from pygame.locals import *
# from paddle import Paddle

def main():
    pygame.init()
    size = width, height = 640, 480
    black = 0,0,0

    screen = pygame.display.set_mode(size)

    g = Game(width, height)
    g.reset_game()
    paddle1 = Rect(g.paddle1.x, g.paddle1.y, g.paddle1.w, g.paddle1.l)
    paddle2 = Rect(g.paddle2.x, g.paddle2.y, g.paddle2.w, g.paddle2.l)
    
    pygame.key.set_repeat(1,1)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        # update centers of the paddle rectangles
        paddle1.center = (g.paddle1.x, g.paddle1.y)
        paddle2.center = (g.paddle2.x, g.paddle2.y)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            g.move_paddle2(1)
        if keys[pygame.K_UP]:
            g.move_paddle2(-1)
        if keys[pygame.K_s]:
            g.move_paddle1(1)
        if keys[pygame.K_w]:
            g.move_paddle1(-1)


        screen.fill(black)
        pygame.draw.circle(screen, (255,255,255), g.ball.get_position(), g.ball.r)
        pygame.draw.rect(screen, (255,255,255), paddle1)
        pygame.draw.rect(screen, (255,255,255), paddle2)
        pygame.display.flip()
        pygame.time.delay(3)
        g.update()

if __name__ == "__main__":
    main()