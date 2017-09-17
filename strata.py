import cairocffi as cairo
import color
import sequence

def draw():
    
    width = 750
    height = 1334
    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    cr = cairo.Context(ims)

    def layer(color, anchor, head, frequency, amplitude, noise):
        
        values = sequence.get_seq(frequency, amplitude, noise)

        cr.set_source_rgb(color.r, color.g, color.b)
        cr.move_to(0, anchor)
        for x in range(0, len(values)):
            cr.line_to(x * (width / (len(values) - 1)), head + values[x])
        cr.line_to(width, anchor)
        cr.line_to(0, anchor)
        cr.fill()
    
    layers = 8
    colors = sequence.get_color_seq( color.true(3, 193, 54), color.true(46, 97, 102), 4)
    colors += sequence.get_color_seq( color.true( 63, 79, 112), color.true( 23, 23, 70), 4)

    layer(colors[0], height, 0, 2, 0, "noise")
    
    for num in range(0, layers-1):
        layer(colors[num+1], height, height * (float(num + 1)/float(layers)), 5, 10, "noise")

    ims.write_to_png("strata.png")
                       
draw()
