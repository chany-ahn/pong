class Paddle:

    def __init__(self, x, y, width=8, length=50):
        # size of the paddle
        self.l = length
        self.w = width
        # position of the paddle
        self.x = x
        self.y = y

    def move(self, addY):
        self.y += addY
    
    def get_dimensions(self):
        return self.w, self.l