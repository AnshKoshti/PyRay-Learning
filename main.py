from pyray import *
from raylib import *
from os.path import join

# Start the window.
init_window(1536, 864, "Basics")

# importing things for game.
spaceship_texture = load_texture(join("assets", "spaceship.png"))

# Starting point of the code.
while not window_should_close():
    begin_drawing()
    clear_background(BLACK)

    # Basic shape usage.
    draw_line_ex(Vector2(100, 100), Vector2(200, 200), 10.0, RAYWHITE)
    draw_pixel(100, 200, BLUE)
    draw_pixel_v(Vector2(220, 220), WHITE)
    draw_circle_v(Vector2(480, 320), 200, YELLOW)
    draw_circle(450, 300, 100, GREEN)

    # Display images.
    draw_texture(spaceship_texture, 0, 0, WHITE)

    end_drawing()

close_window()
