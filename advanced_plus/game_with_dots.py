import pygame as py

# Initialize Pygame
py.init()

# Set up the screen size
size = (500, 400)
screen = py.display.set_mode(size)

# Main loop
running = True
while running:
    for ev in py.event.get():
        if ev.type == py.QUIT:
            running = False  # Exit the loop if the window is closed
        elif ev.type == py.KEYDOWN:
            if ev.key == py.K_ESCAPE:
                running = False  # Exit the loop if Escape is pressed
        elif ev.type == py.MOUSEBUTTONUP:
            pos = py.mouse.get_pos()
            col = (0, 255, 255)
            py.draw.circle(screen, col, pos, 20, 5)
            py.display.update()

# Quit Pygame
py.quit()
