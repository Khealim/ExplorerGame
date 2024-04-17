from PIL import Image, ImageDraw, ImageFont
import os
import random
import keyboard

# Define image size and color
image_size = (200, 200)  # Width, Height
white_color = (255, 255, 255)  # White color in RGB format
black_color = (0, 0, 0)  # black color in RGB format
red_color = (255, 0, 0)  # red color in RGB format

# Load a font
font_path = "arial.ttf"  # Change this to the path of the font you want to use
font_size = 36
font = ImageFont.truetype(font_path, font_size)
text_position = (50, 50)

matrix_size = 7

def get_number_at_coordinates(x, y):
    rows = matrix_size
    columns = matrix_size
    index = (y - 1) * columns + x    
    return index

def redraw_game(x,y,apple_x,apple_y,score):

    index = get_number_at_coordinates(x,y)
    apple_index = get_number_at_coordinates(apple_x,apple_y)

    for i in range(49):
        # Define filename with the subfolder "game"
        filename = os.path.join("game", f"image_{i+1}.png")
        scorename = os.path.join("game", f"score.png")
        
        # Remove the existing image if it exists
        if i+1 == index or i+1 == apple_index:
            if os.path.exists(filename):
                os.remove(filename)
        
        # Create a new blank image
        if i+1 == index:
            new_image = Image.new("RGB", image_size, black_color)
        elif i+1 == apple_index:
            new_image = Image.new("RGB", image_size, red_color)
        else:
            new_image = Image.new("RGB", image_size, white_color)
        
        # Save the image with the same name in the "game" subfolder
        new_image.save(filename)

    if os.path.exists(scorename):
        os.remove(scorename)
    new_score = Image.new("RGB", image_size, white_color)
    draw = ImageDraw.Draw(new_score)
    draw.text(text_position, str(score), fill="black", font=font)
    new_score.save(scorename)
        

# Define the loop

x = 1
y = 1

apple_x = 3
apple_y = 4
score = 0
redraw_game(x,y,apple_x,apple_y,score)

while True:
    print("Press 'up', 'down', 'left', or 'right' keys (Press 'q' to quit):")
    
    
    index = get_number_at_coordinates(x,y)
    apple_index = get_number_at_coordinates(apple_x,apple_y)
    
    if index == apple_index:
        score += 1
        apple_x = random.randint(1, matrix_size)
        apple_y = random.randint(1, matrix_size)
        apple_index = get_number_at_coordinates(apple_x,apple_y)
        redraw_game(x,y,apple_x,apple_y,score)
        while apple_index == index:
            apple_x = random.randint(1, matrix_size)
            apple_y = random.randint(1, matrix_size)
            apple_index = get_number_at_coordinates(apple_x,apple_y)
            redraw_game(x,y,apple_x,apple_y,score)
    
    print("Current coordinates: " + str(x) + ":" + str(y)) 
    print("Current coordinates: " + str(apple_x) + ":" + str(apple_y)) 
    print("Score: " + str(score))
    
    # Wait for a keypress
    key_pressed = keyboard.read_event(suppress=True).name
    
    # Check the pressed key
    if key_pressed == 'up':
        if 1< y <=matrix_size:
            y -=1
            redraw_game(x,y,apple_x,apple_y,score)
        print("Up key pressed")
    elif key_pressed == 'down':
        if 1<= y <matrix_size:
            y +=1
            redraw_game(x,y,apple_x,apple_y,score)
        print("Down key pressed")
    elif key_pressed == 'left':
        if 1< x <=matrix_size:
            x -=1
            redraw_game(x,y,apple_x,apple_y,score)
        print("Left key pressed")
    elif key_pressed == 'right':
        if 1<= x <matrix_size:
            x +=1
            redraw_game(x,y,apple_x,apple_y,score)
        print("Right key pressed")
    elif key_pressed == 'q':  # Quit the loop if 'q' is pressed
        print("Exiting the loop...")
        break
    else:
        print("Invalid key pressed. Press 'up', 'down', 'left', 'right', or 'q' to quit.")
