COLORS = ['#FF0000', '#FF9900', '#FFFF00', '#00FF00', '#0099FF', '#6633FF']
BRUSH_SIZE = 5
PALETTE_PANEL_WIDTH = 60
brush_color = None
color_positions = []
clear_text = []


def update_brush_color(color):
    global brush_color
    brush_color = color

    # brush preview
    stroke(brush_color)
    fill(brush_color)
    strokeWeight(1)
    circle(PALETTE_PANEL_WIDTH / 2, 123, BRUSH_SIZE)


def setup():
    size(600, 600)
    background('#004477')

    # black panel
    fill('#000000')
    rect(0, 0, PALETTE_PANEL_WIDTH, height)

    # color swatches
    for i, color in enumerate(COLORS):
        sx = int(i % 2) * PALETTE_PANEL_WIDTH / 2
        sy = int(i / 2) * PALETTE_PANEL_WIDTH / 2
        fill(color)
        square(sx, sy, PALETTE_PANEL_WIDTH / 2)
        color_positions.append((sx, sy, PALETTE_PANEL_WIDTH / 2, color))

    update_brush_color(COLORS[2])

    # clear button
    fill('#FFFFFF')
    text('CLEAR', 10, height - 12)


def draw():
    if mousePressed and not is_over(0, 0, PALETTE_PANEL_WIDTH, height):
        stroke(brush_color)
        strokeWeight(BRUSH_SIZE)
        line(mouseX, mouseY, pmouseX, pmouseY)


def is_over(x, y, w, h):
    return mouseX >= x and mouseX <= x + w and mouseY >= y and mouseY <= y + h


def is_over_colors():
    return is_over(0, 0, PALETTE_PANEL_WIDTH, PALETTE_PANEL_WIDTH * len(COLORS) / 2)


def get_color():
    for color_position in color_positions:
        if is_over(color_position[0], color_position[1], color_position[2], color_position[2]):
            return color_position[3]  # color


def mouseClicked():
    if is_over_colors():
        color = get_color()
        update_brush_color(color)
    elif is_over(10, height - 22, textWidth('CLEAR'), 22):
        fill('#004477')
        noStroke()
        rect(PALETTE_PANEL_WIDTH, 0, width, height)
