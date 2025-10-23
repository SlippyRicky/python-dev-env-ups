import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter
import os

# Define colors
MAIN_COLOR = [98, 16, 56]  # Bordeaux
SECOND_COLOR = [250, 250, 250]  # Light grey

# Set the size of the grid
image_size = 1600
block_size = image_size // 8  # Each block is 1/8th of the image size

# Create a grid of blocks
num_blocks = image_size // block_size
grid = np.random.choice(
    [0, 1],
    size=(num_blocks, num_blocks),
    p=[0.3, 0.7]  # 30% chance for 0, 70% for 1
)

# Create an image with the specified block size
image = np.zeros((image_size, image_size, 3), dtype=np.uint8)

# Fill each block with the appropriate color
for i in range(num_blocks):
    for j in range(num_blocks):
        start_i, end_i = i * block_size, (i + 1) * block_size
        start_j, end_j = j * block_size, (j + 1) * block_size
        color = SECOND_COLOR if grid[i, j] == 0 else MAIN_COLOR
        image[start_i:end_i, start_j:end_j] = color

# Apply Gaussian blur to each color channel separately
blurred_image = np.zeros_like(image, dtype=np.float32)
for channel in range(3):
    blurred_image[:, :, channel] = gaussian_filter(
        image[:, :, channel].astype(np.float32), sigma=100, truncate=4.0
)

# Clip and convert back to uint8
blurred_image = np.clip(blurred_image, 0, 255).astype(np.uint8)

# Define the directory for images
images_dir = 'images'
os.makedirs(images_dir, exist_ok=True)

# Find the highest existing version number
version = 1
while True:
    filename = f'PP_v{version}.png'
    filepath = os.path.join(images_dir, filename)
    if not os.path.exists(filepath):
        break
    version += 1

# Save the result using PIL to ensure correct handling
img = Image.fromarray(blurred_image)
img.save(filepath)

print(f"Saved as: {filepath}")
