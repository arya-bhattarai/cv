# 7. Draw a triangle with centroid using OpenCV/OpenGL change its color using mouse/keyboard interface.

import cv2
import numpy as np

# Global variables
triangle_color = (0, 255, 0)  # Initial color (green)

# Function to draw a triangle with centroid
def draw_triangle(image, vertices):
    # Draw the triangle
    cv2.polylines(image, [vertices], isClosed=True, color=triangle_color, thickness=2)
    
    centroid = np.mean(vertices, axis=0, dtype=np.int32)
             
    cv2.circle(image, tuple(centroid), 3, (255, 0, 0), -1)     # centroid - small circle
                                             #blue     #fill
    return image

# Mouse callback function
def mouse_callback(event, x, y, flags, param):
    global triangle_color
    
    if event == cv2.EVENT_LBUTTONDOWN:
        triangle_color = (0, 0, 255)  # Change color - red, when left mouse button
    elif event == cv2.EVENT_RBUTTONDOWN:
        triangle_color = (0, 255, 0)  # Change color - green, when right mouse button

# Create a black canvas
canvas = np.zeros((512, 512, 3), dtype=np.uint8)    #3 cahnnels BGR

triangle_vertices = np.array([[250, 100], [150, 300], [350, 300]], dtype=np.int32)

# Display instructions
print("Left click: Change triangle color to red")
print("Right click: Change triangle color to green")
print("Press any key to exit")

while True:
    # Draw the triangle with centroid
    canvas_with_triangle = draw_triangle(canvas.copy(), triangle_vertices)   #making a copy of the canvas to ensure the original is not modified.

    cv2.imshow('Triangle with Centroid', canvas_with_triangle) # Display the image
    
    cv2.setMouseCallback('Triangle with Centroid', mouse_callback) # Set mouse callback
    
    key = cv2.waitKey(1) & 0xFF # Check for key press
    if key != 255:
        break

cv2.destroyAllWindows()