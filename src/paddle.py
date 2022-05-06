class Paddle:

    def __init__(self, x, y, width=2, length=28):
        # size of the paddle
        self.l = length
        self.w = width
        # position of the paddle
        self.x = x
        self.y = y

    def move(self, addY):
        self.y += addY