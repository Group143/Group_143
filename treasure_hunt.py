# Import the 'time' module and the 'Image' class from the 'PIL' module
import time
from PIL import Image

# Generate a random number
# Get the current time in seconds since the epoch as a floating-point number
current_time = int(time.time())

# Calculate the generated number by taking the current time modulo 100 and adding 50
generated_number = (current_time % 100) + 50

# If the generated number is even, add 10 to it
if generated_number % 2 == 0:
    generated_number += 10

# Print the generated number
print(f"Generated number: {generated_number}")

# Open the image file 'Chapter1.png'
image = Image.open("Chapter1.png")

# Convert the image to RGB format
image = image.convert("RGB")

# Get the image dimensions
width, height = image.size

# Loop through each pixel in the image
for x in range(width):
    for y in range(height):
        # Get the RGB values of the current pixel
        r, g, b = image.getpixel((x, y))

        # Add the generated number to the red (r) value
        r += generated_number

        # Set the RGB values of the current pixel to the new values
        image.putpixel((x, y), (r, g, b))

# Save the modified image as 'chapterlout.png'
image.save("chapterlout.png")

# Calculate the sum of all the red (r) pixel values in the modified image
red_sum = sum(image.getpixel((x, y))[0] for x in range(width) for y in range(height))

# Print the sum of all the red pixel values
print(f"Sum of red pixel values: {red_sum}")