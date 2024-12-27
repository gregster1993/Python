import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Matrix-Style Binary Rain")

# Set the dimensions of the window
width, height = 800, 600
canvas = tk.Canvas(root, width=width, height=height, bg="black")
canvas.pack()

# Settings
font_size = 20
columns = int(width / font_size)
drops = [0 for _ in range(columns)]

# Function to draw the binary rain
def draw_rain():
    canvas.delete("all")  # Clear the canvas
    for i in range(len(drops)):
        # Choose a random binary digit
        char = str(random.choice(['M','A','T','R','I','X']))
        # Calculate x and y positions
        x = i * font_size
        y = drops[i] * font_size
        # Display the binary digit
        canvas.create_text(x, y, text=char, fill="yellowgreen", font=("monospace", font_size, "bold"))
        
        # Randomly reset the drop to create a falling effect
        if y > height or random.random() > 0.95:
            drops[i] = 0
        else:
            drops[i] += 1

    # Call the function again after a short delay
    root.after(50, draw_rain)

# Start the rain effect
draw_rain()

# Run the Tkinter event loop
root.mainloop()
