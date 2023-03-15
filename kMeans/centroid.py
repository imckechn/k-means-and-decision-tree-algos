class Centroid:
    point = []
    w = 0
    x = 0
    y = 0
    z = 0

    def set(self, w,x,y,z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def append_iris(self, iris):
        self.point.append(iris)

    def update_center(self):
        w = 0
        x = 0
        y = 0
        z = 0
        for i in self.point:
            w += i.get_w()
            x += i.get_x()
            y += i.get_y()
            z += i.get_z()

        self.set(w/len(self.point), x/len(self.point), y/len(self.point), z/len(self.point))

    def get_center(self):
        return [self.w, self.x, self.y, self.z]
