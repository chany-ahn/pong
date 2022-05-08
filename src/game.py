from ball import Ball
from paddle import Paddle
import random

class Game:

    def __init__(self, width : int, height : int, offset=10):
        # boundaries of the game board
        self.w = width
        self.h = height
        # score of the two players
        self.score = (0,0)
        # game ball
        self.ball = Ball(self.w//2, self.h//2)

        # paddles
        self.paddle1 = Paddle(offset, height//2)
        self.paddle2 = Paddle(width-offset, height//2)

    def is_scored(self):
        position = self.ball.get_position()
        
        if position[1] >= self.w:
            self.score[1] += 1
        
        if position[0] <= 0:
            self.score[0] += 1

    def collision(self):
        x,y = self.ball.get_position()
        r = self.ball.r

        # check collision with paddles
        if x - r == self.paddle1.x + self.paddle1.w//2 and y <= self.paddle1.y + self.paddle1.l and y >= self.paddle1.y - self.paddle1.l:
            self.ball.dx = -self.ball.dx
        
        if x + r == self.paddle2.x - self.paddle2.w//2 and y <= self.paddle2.y + self.paddle2.l and y >= self.paddle2.y - self.paddle2.l:
            self.ball.dx = -self.ball.dx

        # change y component of the velocity if a collision on the top or bottom
        if y == r or y == self.h - r:
            self.ball.dy = -self.ball.dy

        # change x cmoponent of the velocity if a collision on right or left
        if x == r or x == self.w -r:
            self.ball.dx = -self.ball.dx

    # function used to reset the game
    def reset_game(self):
        init_velocity = random.choice([[1,1],[1,-1],[-1,1],[-1,-1]])

        self.ball.set_velocity(init_velocity[0], init_velocity[1])

        self.score = (0,0)
    
    # movement of each paddle
    def move_paddle1(self, addY):

        if self.paddle1.y-self.paddle1.l//2 > 0 and self.paddle1.y+self.paddle1.l//2 < self.h:
            self.paddle1.move(addY)
        
        if self.paddle1.y-self.paddle1.l//2 == 0 and addY > 0:
            self.paddle1.move(addY)

        if self.paddle1.y+self.paddle1.l//2 == self.h and addY < 0:
            self.paddle1.move(addY)
    

    def move_paddle2(self, addY):
        if self.paddle2.y - self.paddle2.l // 2 > 0 and self.paddle2.y+self.paddle2.l//2 < self.h:
            self.paddle2.move(addY)

        if self.paddle2.y-self.paddle2.l//2 == 0 and addY > 0:
            self.paddle2.move(addY)

        if self.paddle2.y+self.paddle2.l//2 == self.h and addY < 0:
            self.paddle2.move(addY)
        
    # update per game loop
    def update(self):
        self.ball.move()
        self.collision()




g = Game(10, 11)