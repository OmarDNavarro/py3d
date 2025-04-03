# transformation.py
import numpy as np

def rotate_x(points, angle):
    """Rotate points around the X-axis."""
    cos_theta = np.cos(angle)
    sin_theta = np.sin(angle)
    
    rotation_matrix = np.array([
        [1, 0, 0],
        [0, cos_theta, -sin_theta],
        [0, sin_theta, cos_theta]
    ])

    return np.dot(points, rotation_matrix.T)

def rotate_y(points, angle):
    """Rotate points around the Y-axis."""
    cos_theta = np.cos(angle)
    sin_theta = np.sin(angle)
    
    rotation_matrix = np.array([
        [cos_theta, 0, sin_theta],
        [0, 1, 0],
        [-sin_theta, 0, cos_theta]
    ])

    return np.dot(points, rotation_matrix.T)

def rotate_z(points, angle):
    """Rotate points around the Z-axis."""
    cos_theta = np.cos(angle)
    sin_theta = np.sin(angle)
    
    rotation_matrix = np.array([
        [cos_theta, -sin_theta, 0],
        [sin_theta, cos_theta, 0],
        [0, 0, 1]
    ])

    return np.dot(points, rotation_matrix.T)

def scale(points, scale):
    
    scale_matrix = np.array([
        [scale, 0, 0],
        [0, scale, 0],
        [0, 0, scale]
    ])

    return np.dot(points, scale_matrix.T)

