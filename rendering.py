# rendering.py

import pygame
import numpy as np
import constants

def project_point(point, camera_pos, fov=200, scaling_factor=1000, epsilon=0.0001, near_clip=0.1):
    """Project a 3D point onto a 2D plane using FOV instead of fixed focal length."""
    x, y, z = point - camera_pos

    # Compute focal length from FOV (convert degrees to radians)
    focal_length = 1 / np.tan(np.radians(fov) / 2)

    # Apply projection formula
    x_2d = int(constants.HALF_WIDTH + x / (z + focal_length) * scaling_factor)
    y_2d = int(constants.HALF_HEIGHT - y / (z + focal_length) * scaling_factor)
    
    return (x_2d, y_2d)


def draw_object(object, camera_pos, screen):
    """Draws a 3D object using its vertices and edges."""
    
    vertices, edges, position = object  # Extract from tuple

    # Apply translation (move object in world space)
    transformed_vertices = vertices + position

    # Project all points relative to the camera
    projected_points = [project_point(point, camera_pos) for point in transformed_vertices]

    # Draw vertices
    for point in projected_points:
        pygame.draw.circle(screen, constants.WHITE, point, 3)

    # Draw edges
    for edge in edges:
        pygame.draw.line(screen, constants.WHITE, projected_points[edge[0]], projected_points[edge[1]], 2)
