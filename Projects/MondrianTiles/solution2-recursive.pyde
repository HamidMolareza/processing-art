WIDTH, HEIGHT = 800, 600

MAXIMUM_SUB_DIVISIONS = 1000

# Not too small
MIN_LENGTH = 80

# Space between quads
SPACE_BETWEEN_RECTANGLES = 1

# Canvas Border
EDGE = 10

BACKGROUND_COLOR = 255
STROKE_WEIGHT = 2


def setup():
    size(WIDTH, HEIGHT)
    pixelDensity(2)
    background(BACKGROUND_COLOR)
    stroke(0)
    strokeWeight(STROKE_WEIGHT)
    mondrian(EDGE, EDGE, WIDTH - (EDGE * 2), HEIGHT - (EDGE * 2))


def draw_rectangle(x, y, width, height):
    fill(random(255), random(255), random(255))
    rect(x, y, width, height)


def can_divide(width_or_height, sub_div_index):
    return width_or_height >= (2 * MIN_LENGTH) and sub_div_index <= MAXIMUM_SUB_DIVISIONS


def divide_vertically(x, y, w, h):
    split = int(random(MIN_LENGTH, w - MIN_LENGTH))
    mondrian(x, y, split - SPACE_BETWEEN_RECTANGLES, h)
    mondrian(x + split, y, w - split, h)


def divide_horizontally(x, y, w, h):
    split = int(random(MIN_LENGTH, h - MIN_LENGTH))
    mondrian(x, y, w, split - SPACE_BETWEEN_RECTANGLES)
    mondrian(x, y + split, w, h - split)


subdivision = 0


def mondrian(x, y, w, h):
    global subdivision
    subdivision += 1

    # divide the rectangle horizontally or vertically with a 50% chance
    if random(1) > 0.5:
        if can_divide(h, subdivision):
            divide_horizontally(x, y, w, h)
        elif can_divide(w, subdivision):
            divide_vertically(x, y, w, h)
        else:
            draw_rectangle(x, y, w, h)
    else:
        if can_divide(w, subdivision):
            divide_vertically(x, y, w, h)
        elif can_divide(h, subdivision):
            divide_horizontally(x, y, w, h)
        else:
            draw_rectangle(x, y, w, h)
