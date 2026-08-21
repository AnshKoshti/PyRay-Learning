from pyray import *
from raylib import *
from os.path import join

# Start the window.
# Allow the window to change size
SetConfigFlags(FLAG_WINDOW_RESIZABLE)
init_window(800, 600, "Basics")

# importing things for game.
# spaceship_texture = load_texture(join("assets", "spaceship.png"))
# cowboy_texture = load_texture(join("assets", "animation", "0.png"))

spaceship_image = load_image(join("assets", "spaceship.png"))
image_color_grayscale(spaceship_image)
new_texture = load_texture_from_image(spaceship_image)

cowboy_image = load_image(join("assets", "animation", "0.png"))
image_color_invert(cowboy_image)
new_texture2 = load_texture_from_image(cowboy_image)

# Starting point of the code.
while not window_should_close():
    # Get current width and height dynamically.
    width = GetScreenWidth()
    height = GetScreenHeight()

    begin_drawing()
    clear_background(BLACK)

    # Basic shape usage.
    draw_line_ex(Vector2(100, 100), Vector2(100, 100), 10.0, RAYWHITE)
    draw_pixel(100, 200, BLUE)
    draw_pixel_v(Vector2(200, 300), WHITE)
    draw_circle_v(Vector2(400, 500), 200, YELLOW)
    draw_circle(600, 300, 100, GREEN)

    # Display images.
    # draw_texture(spaceship_texture, 0, 0, WHITE)
    draw_texture_v(new_texture, Vector2(200, 0), WHITE)
    draw_texture_v(new_texture2, Vector2(0, 500), WHITE)

    end_drawing()

close_window()
