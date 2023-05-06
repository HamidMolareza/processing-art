WIDTH, HEIGHT = 800, 600

SUB_DIVISIONS = 1000

# Not too small
MIN_LENGTH = 80

# Space between quads
SPACE_BETWEEN_RECTANGLES = 1

# Subdivision adjustment
SPLITS = [.5, 1, 1.5]

# Canvas Border
EDGE = 10

BACKGROUND_COLOR = 255
STROKE_WEIGHT = 2


def setup():
    size(WIDTH, HEIGHT)
    pixelDensity(2)
    background(BACKGROUND_COLOR)

    # Add the initial rectangle
    rectangles = [[EDGE, EDGE, WIDTH - (EDGE * 2), HEIGHT - (EDGE * 2)]]

    # Start splitting things up
    for _ in range(SUB_DIVISIONS):
        rectangle_index = int(random(len(rectangles)))
        rectangle = rectangles[rectangle_index]

        split = SPLITS[int(random(len(SPLITS)))]

        if random(1) < 0.5:
            if rectangle[2] > MIN_LENGTH:
                # Get new shapes x value (y is same)
                x_split = rectangle[2] / 2 * split

                rectangles.pop(rectangle_index)
                rectangles.append([rectangle[0], rectangle[1], x_split - SPACE_BETWEEN_RECTANGLES, rectangle[3]])
                rectangles.append([rectangle[0] + x_split, rectangle[1], rectangle[2] - x_split, rectangle[3]])
        else:
            if rectangle[3] > MIN_LENGTH:
                y_split = rectangle[3] / 2 * split

                rectangles.pop(rectangle_index)
                rectangles.append([rectangle[0], rectangle[1], rectangle[2], y_split - SPACE_BETWEEN_RECTANGLES])
                rectangles.append([rectangle[0], y_split + rectangle[1], rectangle[2],
                                   rectangle[3] - y_split])

    stroke(0)
    strokeWeight(STROKE_WEIGHT)

    for rectangle in rectangles:
        fill(color(random(255), random(255), random(255)))
        rect(rectangle[0], rectangle[1], rectangle[2], rectangle[3])
