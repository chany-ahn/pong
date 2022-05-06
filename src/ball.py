class Ball:

    def __init__(self, x_coord, y_coord, radius=8):
        # size of ball
        self.r = radius
        # position of ball
        self.x = x_coord
        self.y = y_coord
        # velocity of ball
        self.dx = 0
        self.dy = 0

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def set_velocity(self, new_dx, new_dy):
        self.dx = new_dx
        self.dy = new_dy

    def get_position(self):
        return (self.x, self.y)

    def collision(self):
        pass