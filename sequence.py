import color
import math
import random

def get_color_seq(start, end, frequency):
    seq = []
    for num in range(0, frequency):
        nextColor = color.Color(start.r + (((end.r - start.r) / (frequency - 1)) * num),
                          start.g + (((end.g - start.g) / (frequency - 1)) * num),
                          start.b + (((end.b - start.b) / (frequency - 1)) * num))

        seq.append(nextColor)

    return seq

def get_seq(frequency, amplitude, noise):
    seq = []
    for num in range(0, frequency):
        seq.append(random.randint(0, amplitude * 2))

    return seq