import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Load the input grayscale image
image = cv2.imread('/content/3fa6bc6d-ae9c-4f37-af02-777c9211267a.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded successfully
if image is None:
    print("Error: Could not open or find the image.")
    exit()

# Function to perform image negation
def image_negation(input_image):
    negated_image = 255 - input_image
    return negated_image

# Function to perform image thresholding
def image_thresholding(input_image, threshold_value):
    _, thresholded_image = cv2.threshold(input_image, threshold_value, 255, cv2.THRESH_BINARY)
    return thresholded_image

# Function to perform image gamma correction
def image_gamma_correction(input_image, gamma):
    gamma_corrected_image = np.power(input_image / 255.0, gamma) * 255.0
    gamma_corrected_image = np.uint8(gamma_corrected_image)
    return gamma_corrected_image

# Perform gray level operations
negated_image = image_negation(image)
thresholded_image = image_thresholding(image, 128)
gamma_corrected_image = image_gamma_correction(image, 1.5)

# Display the original and processed images
cv2_imshow(image)
cv2_imshow(negated_image)
cv2_imshow(thresholded_image)
cv2_imshow(gamma_corrected_image)



# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()