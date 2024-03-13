import cv2
import numpy as np
import math

# Create a window
cv2.namedWindow("Rotating Cube", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Rotating Cube", 800, 600)

# Set cube parameters
cube_size = 100
cube_color = (0, 255, 0)
cube_thickness = 2

# Define cube vertices
vertices = np.array([[-1, -1, -1],
                     [1, -1, -1],
                     [1, 1, -1],
                     [-1, 1, -1],
                     [-1, -1, 1],
                     [1, -1, 1],
                     [1, 1, 1],
                     [-1, 1, 1]], dtype=np.float32)

# Define cube edges
edges = [(0, 1), (1, 2), (2, 3), (3, 0),
         (4, 5), (5, 6), (6, 7), (7, 4),
         (0, 4), (1, 5), (2, 6), (3, 7)]

# Create a rotation matrix
angle = 0
while True:
    rotation_matrix = np.array([[math.cos(angle), -math.sin(angle), 0],
                                [math.sin(angle), math.cos(angle), 0],
                                [0, 0, 1]], dtype=np.float32)

    # Rotate the cube vertices
    rotated_vertices = np.dot(vertices, rotation_matrix)

    # Project the 3D points to 2D
    projected_vertices = (rotated_vertices[:, :2] * cube_size + np.array([400, 300])).astype(int)

    # Create a black image
    frame = np.zeros((600, 800, 3), dtype=np.uint8)

    # Draw cube edges
    for edge in edges:
        pt1 = tuple(projected_vertices[edge[0]])
        pt2 = tuple(projected_vertices[edge[1]])
        cv2.line(frame, pt1, pt2, cube_color, cube_thickness)

    # Display the frame
    cv2.imshow("Rotating Cube", frame)

    # Wait for a moment and update the angle
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

    angle += 0.02

# release the window
cv2.destroyAllWindows()
