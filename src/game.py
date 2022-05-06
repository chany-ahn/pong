from ball import Ball
from paddle import Paddle

class Game:

    def __init__(self, width : int, height : int):
        # boundaries of the game board
        self.w = width
        self.h = height
        # score of the two players
        self.score = (0,0)
        # game ball
        self.ball = Ball(self.w//2, self.h//2)

        # paddles
        self.paddle1 = Paddle(2, height//2)
        self.paddle2 = Paddle(width-2, height//2)


    def is_scored(self) -> bool:
        position = self.ball.get_position()

g = Game(10, 11)