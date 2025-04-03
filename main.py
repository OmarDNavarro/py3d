import pygame
import numpy as np

import transformation

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 1920, 1080
HALF_WIDTH, HALF_HEIGHT = WIDTH / 2, HEIGHT / 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
WHITE, BLACK = (255, 255, 255), (0, 0, 0)

# Constants
CAMERA_SPEED = 0.1
ROTATION_SPEED = 0.03
MAX_ROTATION = 2 * np.pi


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

def project_point(point, camera_pos, fov=200, scaling_factor=1000, epsilon=0.0001, near_clip=0.1):
    """Project a 3D point onto a 2D plane using FOV instead of fixed focal length."""
    x, y, z = point - camera_pos

    # Compute focal length from FOV (convert degrees to radians)
    focal_length = 1 / np.tan(np.radians(fov) / 2)

    # Apply projection formula
    x_2d = int(HALF_WIDTH + x / (z + focal_length) * scaling_factor)
    y_2d = int(HALF_HEIGHT - y / (z + focal_length) * scaling_factor)
    
    return (x_2d, y_2d)


def draw_object(object, camera_pos):
    """Draws a 3D object using its vertices and edges."""
    
    vertices, edges, position = object  # Extract from tuple

    # Apply translation (move object in world space)
    transformed_vertices = vertices + position

    # Project all points relative to the camera
    projected_points = [project_point(point, camera_pos) for point in transformed_vertices]

    # Draw vertices
    for point in projected_points:
        pygame.draw.circle(screen, WHITE, point, 3)

    # Draw edges
    for edge in edges:
        pygame.draw.line(screen, WHITE, projected_points[edge[0]], projected_points[edge[1]], 2)


def main():
    """Main loop for rendering the cube."""
    running = True

    objects = list()
    for i in range(9):
        objects.append(tetrahedron((i * 4, 5, 0)))
        objects.append(cube((i*4, 0, 0)))
        objects.append(pyramid((i*4, -5, 0)))

    # Define camera position (starting at origin)
    camera_pos = np.array([15.0, 0.0, -20.0])  # Start at z = -5 to see the object

    rotation_x, rotation_y, rotation_z = 0, 0, 0

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get user input for rotations
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            camera_pos[2] += CAMERA_SPEED
        if keys[pygame.K_s]:
            camera_pos[2] -= CAMERA_SPEED

        if keys[pygame.K_a]:
            camera_pos[0] -= CAMERA_SPEED
        if keys[pygame.K_d]: 
            camera_pos[0] += CAMERA_SPEED

        if keys[pygame.K_q]:
            camera_pos[1] -= CAMERA_SPEED
        if keys[pygame.K_e]: 
            camera_pos[1] += CAMERA_SPEED

        rotation_x += ROTATION_SPEED
        rotation_y += ROTATION_SPEED
        rotation_z += ROTATION_SPEED

        # Wrap the angles to keep them in the range [0, 2π]
        rotation_x %= MAX_ROTATION
        rotation_y %= MAX_ROTATION
        rotation_z %= MAX_ROTATION

        # Apply rotations to each object
        for object in objects:
            vertices, edges, position = object
            
            # Apply rotation in order X -> Y
            rotated_vertices = transformation.rotate_x(vertices, rotation_x)
            rotated_vertices = transformation.rotate_y(rotated_vertices, rotation_y)

            # Create the transformed object with rotated vertices
            transformed_object = (rotated_vertices, edges, position)

            # Draw the transformed object
            draw_object(transformed_object, camera_pos)
        
        pygame.display.flip()
        clock.tick(60) # 60 FPS
    
    pygame.quit()

if __name__ == "__main__":
    main()
