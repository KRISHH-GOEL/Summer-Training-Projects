import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# ==========================
# Load Image
# ==========================
img = Image.open("image.png")
img_array = np.array(img)

# Print image dimensions
print("Image Shape:", img_array.shape)

# ==========================
# Display Original Image
# ==========================
plt.figure(figsize=(6, 6))
plt.imshow(img_array)
plt.title("Original Image")
plt.axis("off")
plt.show()

# ==================================================
# Part 1 : Modify Image Colors
# ==================================================
modified = img_array.copy()

# Modify RGB values
modified[:, :, 0] = np.clip(modified[:, :, 0] - 100, 0, 255)  # Red
modified[:, :, 1] = np.clip(modified[:, :, 1] + 50, 0, 255)   # Green
modified[:, :, 2] = np.clip(modified[:, :, 2] + 50, 0, 255)   # Blue

# Display Modified Image
plt.figure(figsize=(6, 6))
plt.imshow(modified)
plt.title("Modified Image")
plt.axis("off")
plt.show()

# ==================================================
# Part 2 : Divide Image into RGB Quadrants
# ==================================================
quadrant = img_array.copy()

# Get image dimensions
height, width, _ = quadrant.shape

# Find center
mid_h = height // 2
mid_w = width // 2

# Top-Left -> Red Only
quadrant[:mid_h, :mid_w, 1] = 0
quadrant[:mid_h, :mid_w, 2] = 0

# Top-Right -> Green Only
quadrant[:mid_h, mid_w:, 0] = 0
quadrant[:mid_h, mid_w:, 2] = 0

# Bottom-Left -> Blue Only
quadrant[mid_h:, :mid_w, 0] = 0
quadrant[mid_h:, :mid_w, 1] = 0

# Bottom-Right -> Original (No changes)

# Display RGB Quadrants
plt.figure(figsize=(6, 6))
plt.imshow(quadrant)
plt.title("Red | Green | Blue | Original")
plt.axis("off")
plt.show()
