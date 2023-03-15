class Iris:
    w = 0
    x = 0
    y = 0
    z = 0
    name = ""

    def __init__(self, type, w, x, y, z):
        self.w = float(w)
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.name = type

    def get_type(self):
        return self.name

    def get_w(self):
        return self.w

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def get_coordinates(self):
        return [self.w, self.x, self.y, self.z]
