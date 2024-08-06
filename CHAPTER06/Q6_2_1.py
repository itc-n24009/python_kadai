class Cylinder:
    pi = 3.14
    def __init__(self,hankei=1,takasa=1):
        self.hankei = float(hankei)
        self.takasa = float(takasa)
    def base_area(self):
        pi = Cylinder.pi
        r = self.hankei
        return pi * r * r
    def side_area(self):
        pi = Cylinder.pi
        r = self.hankei
        h = self.takasa
        return 2 * pi * r * h
    def surface_area(self):
        b = self.base_area()
        s = self.side_area()
        return 2 * b + s
    def volume(self):
        b = self.base_area()
        h = self.takasa
        return b * h
    def result(self):
        r = self.hankei
        h = self.takasa
        s = self.surface_area()
        v = self.volume()
        print(f"半径: {r}, 高さ: {h}, 表面積: {s}, 体積: {v}")
