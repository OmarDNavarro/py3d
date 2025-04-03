# shape.py

import numpy as np

def cube(position=(0, 0, 0)):
    """Generates a cube with vertices, edges, and position as a tuple."""
    vertices = np.array([
        [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
        [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
    ])

    edges = [
        [0, 1], [1, 2], [2, 3], [3, 0],  # Front face
        [4, 5], [5, 6], [6, 7], [7, 4],  # Back face
        [0, 4], [1, 5], [2, 6], [3, 7]   # Connecting edges
    ]

    # Return as a tuple (vertices, edges, position)
    return (vertices, edges, np.array(position))


def pyramid(position=(0, 0, 0)):
    points_3d = np.array([
        [-1, -1, 0], [1, -1, 0], [1, 1, 0], [-1, 1, 0],
        [0, 0, 1]
    ])

    edges = [
        [0, 1], [1, 2], [2, 3], [3, 0], # Base
        [0, 4], [1, 4], [2, 4], [3, 4]  # Triangle sides
    ]

    return (points_3d, edges, np.array(position))

def tetrahedron(position=(0, 0, 0)):
    """Generates a tetrahedron with vertices, edges, and position as a tuple."""
    vertices = np.array([
        [1, 1, 1],   # Vertex 0
        [-1, -1, 1], # Vertex 1
        [-1, 1, -1], # Vertex 2
        [1, -1, -1]  # Vertex 3
    ])

    edges = [
        [0, 1], [1, 2], [2, 3], [3, 0],  # Base edges
        [0, 2], [1, 3], [0, 3], [1, 2]   # Sides
    ]

    return (vertices, edges, np.array(position))