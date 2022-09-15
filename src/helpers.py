import pygame, io

def load_and_scale_svg(filename, scale):
    svg_string = open(filename, "rt").read()

    svg_string = svg_string.replace('transform="scale(2)"', f'transform="scale({scale})"')

    start = svg_string.find('transform="scale(2)')
    if start > 0:
        svg_string = svg_string[:start] + f' transform="scale({scale})"' + svg_string[start:]
    return pygame.image.load(io.BytesIO(svg_string.encode()))