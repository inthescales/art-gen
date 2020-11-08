import sys
import cairocffi as cairo

import src.color as color
import src.sequence as sequence

dest = "strata.png"
width = 500
height = 500

if len(sys.argv) > 1:
    dest = sys.argv[1]

if len(sys.argv) > 2:
    width = int(sys.argv[2])

if len(sys.argv) > 3:
    height = int(sys.argv[3])

def draw():
    global dest, width, height
    
    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    cr = cairo.Context(ims)

    def layer(color, anchor, head, frequency, amplitude, noise):
        
        values = sequence.get_seq(frequency, amplitude, noise)
        values[len(values)-1] = values[0]

        cr.set_source_rgb(color.r, color.g, color.b)
        cr.move_to(0, anchor)

        for x in range(0, len(values)):
            cr.line_to(x * (width / float(len(values) - 1)), head + values[x])
        cr.line_to(width, anchor)
        cr.line_to(0, anchor)
        cr.fill()
    
    layers = 8
    #moss
    #colors = sequence.get_color_seq( color.rgb(3, 193, 54), color.rgb(46, 97, 102), 4)
    #colors += sequence.get_color_seq( color.rgb( 63, 79, 112), color.rgb( 23, 23, 70), 4)
    #moss-mod
    #colors = sequence.get_color_seq( color.rgb(3, 193, 54), color.rgb( 10, 10, 45), layers)
    #moss-bottom
    #colors = sequence.get_color_seq( color.rgb( 23, 23, 60), color.rgb(0, 0, 20), layers)
    #vent
    colors = sequence.get_color_seq( color.rgb(222, 14, 1), color.rgb(102, 45, 60), 4)
    colors += sequence.get_color_seq( color.rgb( 44, 53, 77), color.rgb( 28, 28, 70), 4)
    #surf
    #colors = sequence.get_color_seq( color.rgb(244, 200, 88), color.rgb(183, 127, 5), 3)
    #colors += [color.rgb(214, 251, 252)]
    #colors += sequence.get_color_seq( color.rgb( 47, 233, 237), color.rgb( 15, 87, 221), 4)

    layer(colors[0], height, 0, 2, 0, "noise")
    
    for num in range(0, layers-1):
        layer(colors[num+1], height, height * (float(num + 1)/float(layers)), 5, 25, "noise")

    ims.write_to_png(dest)
                       
draw()
