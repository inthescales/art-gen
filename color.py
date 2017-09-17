class Color:
        def __init__(self, r, g, b, a=1.0):
            self.r = r
            self.g = g
            self.b = b
            self.a = a
        
        def string(self):
            print("(" + str(self.r) + ", " + str(self.g) + ", " + str(self.b) + ", " + str(self.a) + ")")
            
def true(r, g, b, a=1.0):
    return Color(float(r) / 256.0, float(g) / 256.0, float(b) / 256.0, a)
