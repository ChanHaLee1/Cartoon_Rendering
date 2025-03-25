import cv2
import numpy as np

def cartoonify(image_path):
    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not load image.")
        return
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply median blur to reduce noise
    gray = cv2.medianBlur(gray, 5)
    
    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                  cv2.THRESH_BINARY, 9, 9)
    
    # Convert the image to color using bilateral filter to smooth colors
    color = cv2.bilateralFilter(img, 9, 300, 300)
    
    # Combine color image with edges mask
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    
    # Display the result
    cv2.imshow("Cartoon", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 실행 예제
cartoonify('chopper_image.jpg')