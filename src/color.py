class Color:
        def __init__(self, r, g, b, a=1.0):
            self.r = r
            self.g = g
            self.b = b
            self.a = a
            
            hsv = rgb_to_hsv(r, g, b)
            self.h = hsv[0]
            self.s = hsv[1]
            self.v = hsv[2]
        
        def string_rgb(self):
            return "(" + str(self.r) + ", " + str(self.g) + ", " + str(self.b) + ", " + str(self.a) + ")"
            
        def string_hsv(self):
            return  "(" + str(self.h) + ", " + str(self.s) + ", " + str(self.v) + ", " + str(self.a) + ")"
            
def rgb(r, g, b, a=1.0, depth=255.0):
    return Color(r / depth, g / depth, b / depth, a)

def hsv(h, s, v, a=1.0):
    rgb = hsv_to_rgb(h, s / 100, v / 100)
    return Color(rgb[0], rgb[1], rgb[2], a)

def hsv_to_rgb(h, s, v):
    c = v * s
    x = c * (1 - abs((h / d) % 2) - 1)
    m = v - c
    
    def get_tuple(c, x):
        if h < d:
            return (c, x, 0)
        elif h < d * 2.0:
            return (x, c, 0)
        elif h < d * 3.0:
            return (0, c, x)
        elif h < d * 4.0:
            return (0, x, c)
        elif h < d * 5.0:
            return (x, 0, c)
        else:
            return (c, 0, x)
        
    tup = get_tuple(c, x)
    return (tup[0], tup[1], tup[2])

def rgb_to_hsv(r, g, b):
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delt = cmax - cmin
    
    def get_hue(delt, cmax, cmin):
        
        val = 0
        
        if delt == 0:
            return 0
        elif cmax == r:
            val = ((g - b)/delt)
        elif cmax == g:
            val = ((b - r)/delt)
        elif cmax == b:
            val = ((r - g)/delt)

        val = (val * 60) % 360
            
        return val
    
    def get_sat(delt, cmax):
        if cmax == 0:
            return 0
        else:
            return (delt/cmax)
        
    return (get_hue(delt, cmax, cmin), get_sat(delt, cmax), cmax)




    