from PIL import Image
import numpy as np

image = Image.open("homework\images\birds.jpg")
image_array = np.array(image)

flipped_horizontally = np.fliplr(image_array)

flipped_vertically = np.flipud(image_array)

Image.fromarray(flipped_horizontally).save("flipped_horizontally.jpg")
Image.fromarray(flipped_vertically).save("flipped_vertically.jpg")

# Generate random noise
noise = np.random.randint(0, 50, image_array.shape, dtype=np.uint8)

# Add noise and clip to [0, 255]
noisy_image = np.clip(image_array + noise, 0, 255)

# Save
Image.fromarray(noisy_image).save("noisy_image.jpg")

# Increase brightness of red channel by 40
brightened_image = image_array.copy()
brightened_image[:, :, 0] = np.clip(brightened_image[:, :, 0] + 40, 0, 255)

# Save
Image.fromarray(brightened_image).save("brightened_image.jpg")

# Get image dimensions
h, w, _ = image_array.shape
center_x, center_y = w // 2, h // 2

# Define mask size
mask_size = 100

# Apply black mask
masked_image = image_array.copy()
masked_image[center_y - mask_size//2:center_y + mask_size//2, 
             center_x - mask_size//2:center_x + mask_size//2] = [0, 0, 0]

# Save
Image.fromarray(masked_image).save("masked_image.jpg")