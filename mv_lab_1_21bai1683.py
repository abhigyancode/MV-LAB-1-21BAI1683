# -*- coding: utf-8 -*-
"""MV LAB 1 21BAI1683.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Kf7od0oSdVdw8Vc5UoHBBivwBsxgFeT7

AS-1(a)

TASK-1
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read the Image
image_path = '/th.jpg'  # Replace with your image file path
image = cv2.imread(image_path)

# Convert the image from BGR (OpenCV default) to RGB for displaying
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_rgb

# Step 2: Compute Basic Statistics
# Calculate the mean and standard deviation for each color channel
mean, stddev = cv2.meanStdDev(image)

# Calculate the histogram for each color channel
colors = ('b', 'g', 'r')  # OpenCV uses BGR by default
for i, color in enumerate(colors):
    histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(histogram, color=color)
    plt.xlim([0, 256])

plt.title('Histogram for each color channel')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()

# Print the mean and standard deviation
print(f"Mean (BGR): {mean.flatten()}")
print(f"Standard Deviation (BGR): {stddev.flatten()}")

# Step 3: Convert Color Spaces
# Convert to HSV color space
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Convert to Lab color space
image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)

# Display the original and converted images
plt.figure(figsize=(10, 10))

# Original Image
plt.subplot(1, 3, 1)
plt.imshow(image_rgb)
plt.title('Original Image (RGB)')
plt.axis('off')

# HSV Image
plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(image_hsv, cv2.COLOR_HSV2RGB))
plt.title('Image in HSV Color Space')
plt.axis('off')

# Lab Image
plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(image_lab, cv2.COLOR_Lab2RGB))
plt.title('Image in Lab Color Space')
plt.axis('off')

plt.show()

"""TASK-2"""

import cv2
import matplotlib.pyplot as plt

# Step 1: Read the Image (Load as Grayscale)
image_path = '/th.jpg'  # Replace with your grayscale image file path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Step 2: Apply Thresholding
# Use a fixed threshold value of 127 (you can adjust this value)
threshold_value = 127
_, segmented_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

# Step 3: Display Results
plt.figure(figsize=(10, 5))

# Original Image
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image (Grayscale)')
plt.axis('off')

# Segmented Image
plt.subplot(1, 2, 2)
plt.imshow(segmented_image, cmap='gray')
plt.title(f'Segmented Image (Threshold = {threshold_value})')
plt.axis('off')

plt.show()

"""TASK-3"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read the Image (Load as Grayscale)
image_path = '/th.jpg'  # Replace with your grayscale image file path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Step 2: Convert Grayscale Image to "Color" Space
# Here we can treat different intensity levels as different "colors"
# However, there's no need to convert to HSV as it's a grayscale image
# We will just directly apply thresholding based on intensity
# If needed, we can stack grayscale into 3 channels to mimic RGB
image_colored = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

# Step 3: Apply Intensity Thresholding
# Define the intensity range to segment (e.g., bright areas)
lower_bound = 150  # Lower intensity bound
upper_bound = 255  # Upper intensity bound

# Create a mask that captures only the specified intensity range
mask = cv2.inRange(image, lower_bound, upper_bound)

# Apply the mask to the "colored" image to segment the specific intensity range
segmented_image = cv2.bitwise_and(image_colored, image_colored, mask=mask)

# Step 4: Display Results
plt.figure(figsize=(15, 10))

# Original Image
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image (Grayscale)')
plt.axis('off')

# Masked Image (Binary)
plt.subplot(1, 3, 2)
plt.imshow(mask, cmap='gray')
plt.title('Mask (Intensity Thresholding)')
plt.axis('off')

# Segmented Image
plt.subplot(1, 3, 3)
segmented_image_rgb = cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB)  # Convert to RGB for display
plt.imshow(segmented_image_rgb)
plt.title('Segmented Image (Intensity-Based)')
plt.axis('off')

plt.show()

"""AS-1(b)

TASK-1
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load a grayscale image
image_path = '/images.jpg'  # Replace with your image file path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Step 2: Apply the image negative transformation
negative_image = 255 - image

# Step 3: Display the original and the negative image
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(negative_image, cmap='gray')
plt.title('Negative Image')
plt.axis('off')

plt.show()

"""TASK-2"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load a grayscale image
image_path = '/images.jpg'  # Replace with your image file path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Step 2: Apply gamma correction
gamma_values = [0.5, 1.0, 2.0]
gamma_corrected_images = [(image / 255.0) ** gamma * 255 for gamma in gamma_values]

# Step 3: Display the original and the gamma-corrected images
plt.figure(figsize=(15, 5))

plt.subplot(1, 4, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

for i, gamma in enumerate(gamma_values):
    plt.subplot(1, 4, i + 2)
    plt.imshow(np.uint8(gamma_corrected_images[i]), cmap='gray')
    plt.title(f'Gamma = {gamma}')
    plt.axis('off')

plt.show()

"""TASK-3"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load a grayscale image
image_path = '/images.jpg'  # Replace with your image file path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Step 2: Apply log transformation
c = 255 / np.log(1 + np.max(image))  # Calculate scaling constant
log_transformed_image = c * np.log(1 + image)

# Normalize to 0-255 and convert to uint8
log_transformed_image = np.uint8(log_transformed_image)

# Step 3: Display the original and the log-transformed image
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(log_transformed_image, cmap='gray')
plt.title('Log Transformed Image')
plt.axis('off')

plt.show()

"""TASK-4"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load a grayscale image
image_path = '/images.jpg'  # Replace with your image file path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply transformations
negative_image = 255 - image
gamma_corrected_image = np.uint8((image / 255.0) ** 2.0 * 255)
c = 255 / np.log(1 + np.max(image))
log_transformed_image = np.uint8(c * np.log(1 + image))

# Step 3: Display the original image alongside the transformed images
plt.figure(figsize=(20, 5))

plt.subplot(1, 4, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(negative_image, cmap='gray')
plt.title('Negative Image')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(gamma_corrected_image, cmap='gray')
plt.title('Gamma Corrected (γ=2.0)')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.imshow(log_transformed_image, cmap='gray')
plt.title('Log Transformed Image')
plt.axis('off')

plt.show()

"""TASK-5"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load a color image
image_path = '/images.jpg'  # Replace with your image file path
image = cv2.imread(image_path)

# Step 2: Split the image into its R, G, and B channels
B, G, R = cv2.split(image)

# Step 3: Apply image negative, gamma correction, and log transformation to each channel

# Image Negative
B_negative = 255 - B
G_negative = 255 - G
R_negative = 255 - R

# Gamma Correction with γ=2.0
gamma = 2.0
B_gamma_corrected = np.uint8((B / 255.0) ** gamma * 255)
G_gamma_corrected = np.uint8((G / 255.0) ** gamma * 255)
R_gamma_corrected = np.uint8((R / 255.0) ** gamma * 255)

# Log Transformation
c_B = 255 / np.log(1 + np.max(B))
c_G = 255 / np.log(1 + np.max(G))
c_R = 255 / np.log(1 + np.max(R))

B_log_transformed = np.uint8(c_B * np.log(1 + B))
G_log_transformed = np.uint8(c_G * np.log(1 + G))
R_log_transformed = np.uint8(c_R * np.log(1 + R))

# Step 4: Merge the channels back together
negative_image = cv2.merge([B_negative, G_negative, R_negative])
gamma_corrected_image = cv2.merge([B_gamma_corrected, G_gamma_corrected, R_gamma_corrected])
log_transformed_image = cv2.merge([B_log_transformed, G_log_transformed, R_log_transformed])

# Step 5: Display the original and the transformed images
plt.figure(figsize=(20, 10))

plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(negative_image, cv2.COLOR_BGR2RGB))
plt.title('Negative Image')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(gamma_corrected_image, cv2.COLOR_BGR2RGB))
plt.title('Gamma Corrected (γ=2.0)')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(cv2.cvtColor(log_transformed_image, cv2.COLOR_BGR2RGB))
plt.title('Log Transformed Image')
plt.axis('off')

plt.show()

"""AS-1(c)

TASK-1
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load and Display an Image
image_path = '/th.jpg'  # Replace with your grayscale image path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Display the original image
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Plot the histogram of the original image
plt.subplot(1, 2, 2)
plt.hist(image.ravel(), 256, [0, 256])
plt.title('Histogram of Original Image')
plt.show()

# Step 2: Calculate and Plot Histogram Manually
histogram, bin_edges = np.histogram(image, bins=256, range=(0, 255))

plt.figure(figsize=(5, 4))
plt.plot(bin_edges[0:-1], histogram)
plt.title("Manual Histogram Calculation")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.show()

# Step 3: Calculate Cumulative Distribution Function (CDF)
cdf = histogram.cumsum()
cdf_normalized = cdf * histogram.max() / cdf.max()

plt.figure(figsize=(5, 4))
plt.plot(cdf_normalized, color='b')
plt.hist(image.ravel(), 256, [0, 256], color='r', alpha=0.5)
plt.legend(('CDF', 'Histogram'), loc='upper left')
plt.title('CDF and Histogram of Original Image')
plt.show()

# Step 4: Apply Histogram Equalization
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')

equalized_image = cdf[image]

# Display the equalized image and its histogram
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.hist(equalized_image.ravel(), 256, [0, 256])
plt.title('Histogram of Equalized Image')
plt.show()

# Step 5: Compare Results
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.show()

"""TASK-2"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load an Image
image_path = '/th.jpg'  # Replace with your image path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Standard Histogram Equalization
equalized_image = cv2.equalizeHist(image)

# Step 1: Implement Adaptive Histogram Equalization (AHE)
# Using OpenCV's CLAHE for demonstration as AHE is a subset of CLAHE
clahe = cv2.createCLAHE(clipLimit=40.0, tileGridSize=(8,8))
ahe_image = clahe.apply(image)

# Step 2: Implement Contrast Limited Adaptive Histogram Equalization (CLAHE)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
clahe_image = clahe.apply(image)

# Step 3: Compare Results
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Standard Histogram Equalization')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(ahe_image, cmap='gray')
plt.title('Adaptive Histogram Equalization (AHE)')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(clahe_image, cmap='gray')
plt.title('Contrast Limited AHE (CLAHE)')
plt.axis('off')

plt.show()

"""TASK-3"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load a Color Image
image_path = '/th.jpg'  # Replace with your color image path
image = cv2.imread(image_path)

# Step 2: Separate Color Channels
b, g, r = cv2.split(image)

# Step 3: Apply Histogram Equalization to Each Channel
b_eq = cv2.equalizeHist(b)
g_eq = cv2.equalizeHist(g)
r_eq = cv2.equalizeHist(r)

# Step 4: Reconstruct the Color Image
equalized_image = cv2.merge([b_eq, g_eq, r_eq])

# Step 5: Compare Results
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(equalized_image, cv2.COLOR_BGR2RGB))
plt.title('Equalized Color Image')
plt.axis('off')

plt.show()

"""TASK-4"""

# Example: Apply histogram equalization to medical images (X-ray)
image_path = '/x-ray-skull-from-right-side.jpg'  # Replace with your X-ray image path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

equalized_image = cv2.equalizeHist(image)

# Compare the original and equalized images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original X-ray Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized X-ray Image')
plt.axis('off')

plt.show()

"""TASK-5"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load a Low Contrast Image
image_path = '/13508063773_5edbca4946_b.jpg'  # Replace with your low contrast image path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Step 2: Apply Histogram Equalization
equalized_image = cv2.equalizeHist(image)

# Step 3: Analyze Results
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Low Contrast Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.show()

"""TASK-6"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load and Resize Image to Different Scales
image_path = '/th.jpg'  # Replace with your grayscale image path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Rescale the image to 50%, 100%, and 200% of original size
scales = [0.5, 1.0, 2.0]
rescaled_images = [cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR) for scale in scales]

# Step 2: Apply Histogram Equalization
equalized_images = [cv2.equalizeHist(rescaled_image) for rescaled_image in rescaled_images]

# Step 3: Compare Results
plt.figure(figsize=(15, 10))

for i, scale in enumerate(scales):
    plt.subplot(2, 3, i + 1)
    plt.imshow(rescaled_images[i], cmap='gray')
    plt.title(f'Original Image (Scale={int(scale*100)}%)')
    plt.axis('off')

    plt.subplot(2, 3, i + 4)
    plt.imshow(equalized_images[i], cmap='gray')
    plt.title(f'Equalized Image (Scale={int(scale*100)}%)')
    plt.axis('off')

plt.show()

"""TASK-7"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load Images with Varying Levels of Detail and Contrast
image_paths = ['/images.jpg', '/images (1).jpg', '/th.jpg']  # Replace with your image paths
images = [cv2.imread(img_path, cv2.IMREAD_GRAYSCALE) for img_path in image_paths]

# Step 2: Apply Histogram Equalization
equalized_images = [cv2.equalizeHist(img) for img in images]

# Step 3: Evaluate Enhancement
plt.figure(figsize=(15, 10))

for i, (img, eq_img) in enumerate(zip(images, equalized_images)):
    plt.subplot(len(images), 2, i*2 + 1)
    plt.imshow(img, cmap='gray')
    plt.title(f'Original Image {i+1}')
    plt.axis('off')

    plt.subplot(len(images), 2, i*2 + 2)
    plt.imshow(eq_img, cmap='gray')
    plt.title(f'Equalized Image {i+1}')
    plt.axis('off')

plt.show()

"""TASK-8"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load an Image for Segmentation
image_path = '/th.jpg'  # Replace with your image path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Perform simple thresholding for segmentation
_, segmented_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Step 2: Apply Histogram Equalization and Segmentation
equalized_image = cv2.equalizeHist(image)
_, segmented_eq_image = cv2.threshold(equalized_image, 127, 255, cv2.THRESH_BINARY)

# Step 3: Compare Segmentation Results
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(segmented_image, cmap='gray')
plt.title('Segmented Image')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(segmented_eq_image, cmap='gray')
plt.title('Segmented Equalized Image')
plt.axis('off')

plt.show()