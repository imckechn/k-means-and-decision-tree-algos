class Centroid:
    closest_irises = []
    w = 0
    x = 0
    y = 0
    z = 0
    most_common_iris = ""

    #Sets the location of the centroid
    def set(self, w,x,y,z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z


    #add an iris to its closest irises
    def append_iris(self, iris):
        self.closest_irises.append(iris)


    #Updates the location of the centroid, returns true if it moved, false if it didn't
    def update_center(self):
        moved = False

        if self.closest_irises == []:
            return moved

        w = 0
        x = 0
        y = 0
        z = 0
        for i in self.closest_irises:
            w += i.get_w()
            x += i.get_x()
            y += i.get_y()
            z += i.get_z()

        w = w/len(self.closest_irises)
        x = x/len(self.closest_irises)
        y = y/len(self.closest_irises)
        z = z/len(self.closest_irises)

        if w != self.w or x != self.x or y != self.y or z != self.z:
            self.set(w,x,y,z)
            moved = True

        return moved


    #Returns the location of the centroid
    def get_center(self):
        return [self.w, self.x, self.y, self.z]


    #Returns the number of irises in the centroid
    def get_irises_len(self):
        return len(self.closest_irises)


    #Returns the list of irises in the centroid
    def get_irises(self):
        return self.closest_irises


    #Removes all the irises from the centroid
    def wipe_irises(self):
        self.closest_irises = []


    #Finds the most common iris in its closest irises
    def set_most_common_iris(self):
        score = {}
        for iris in self.closest_irises:
            if iris.get_type() in score.keys():
                score[iris.get_type()] += 1

            else:
                score[iris.get_type()] = 1

        highest = 0
        for key, value in score.items():
            if value > highest:
                highest = value
                self.most_common_iris = key


    # Returns the most common flower in the centroid
    def get_most_common_iris(self):
        return self.most_common_iris