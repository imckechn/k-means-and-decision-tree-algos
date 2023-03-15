class Centroid:
    points = []
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
        self.points.append(iris)


    def update_center(self):
        moved = False

        if self.points == []:
            return moved

        w = 0
        x = 0
        y = 0
        z = 0
        for i in self.points:
            w += i.get_w()
            x += i.get_x()
            y += i.get_y()
            z += i.get_z()

        w = w/len(self.points)
        x = x/len(self.points)
        y = y/len(self.points)
        z = z/len(self.points)

        if w != self.w or x != self.x or y != self.y or z != self.z:
            self.set(w,x,y,z)
            moved = True

        self.points = []
        return moved


    def get_center(self):
        return [self.w, self.x, self.y, self.z]


    def get_points_len(self):
        return len(self.points)