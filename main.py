import cv2
import os


def smooth_and_save(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Apply smoothing using Gaussian blur
    smoothed_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Save the smoothed image
    smoothed_image_path = os.path.splitext(image_path)[0] + "_smoothed.jpg"
    cv2.imwrite(smoothed_image_path, smoothed_image)

    # Apply edge detection using Canny
    edges = cv2.Canny(image, 100, 200)

    # Save the edge-detected image
    edge_image_path = os.path.splitext(image_path)[0] + "_edges.jpg"
    cv2.imwrite(edge_image_path, edges)

    print("Images saved successfully!")


# Specify the path to the image
image_path = "C:/Users/adamk/OneDrive/Desktop/Summer 2023/CS 7375 AI/Assignment 3/fighter_noise_10.jpg"

# Call the function to smooth and save the image
smooth_and_save(image_path)
