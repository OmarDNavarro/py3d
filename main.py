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

# Define rotation speeds
ROTATION_SPEED = 0.05

def cube_generator():
    """Generate 3D cube vertices and edges."""
    points_3d = np.array([
        [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
        [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
    ])
    
    edges = [
        [0, 1], [1, 2], [2, 3], [3, 0],  # Front face
        [4, 5], [5, 6], [6, 7], [7, 4],  # Back face
        [0, 4], [1, 5], [2, 6], [3, 7]   # Connecting edges
    ]
    
    return points_3d, edges

def project_point(point, focal_length=5, scaling_factor=1000, epsilon=0.0001):
    """Project a 3D point onto a 2D plane."""
    x, y, z = point
    x_2d = int(HALF_WIDTH + x / (z + focal_length + epsilon) * scaling_factor)
    y_2d = int(HALF_HEIGHT - y / (z + focal_length + epsilon) * scaling_factor)
    return (x_2d, y_2d)

def draw_object(object_points, object_edges):
    """Draw a wireframe object using projected points."""
    projected_points = [project_point(point) for point in object_points]

    # Draw points
    for point in projected_points:
        pygame.draw.circle(screen, WHITE, point, 10)

    # Draw edges
    for a, b in object_edges:
        pygame.draw.line(screen, WHITE, projected_points[a], projected_points[b], 2)

def main():
    """Main loop for rendering the cube."""
    running = True
    object_points, object_edges = cube_generator()
    rotation_x, rotation_y, rotation_z = 0, 0, 0


    while running:
        screen.fill(BLACK)  # Clear screen

        # Apply Rotations
        rotated_points = transformation.rotate_x(object_points, rotation_x)
        rotated_points = transformation.rotate_y(rotated_points, rotation_y)
        rotated_points = transformation.rotate_z(rotated_points, rotation_z)

        draw_object(rotated_points, object_edges)  # Draw the cube

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get user input for rotations
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            rotation_x += ROTATION_SPEED
        if keys[pygame.K_DOWN]:
            rotation_x -= ROTATION_SPEED

        if keys[pygame.K_LEFT]:
            rotation_y += ROTATION_SPEED
        if keys[pygame.K_RIGHT]:
            rotation_y -= ROTATION_SPEED

        if keys[pygame.K_a]:
            rotation_z += ROTATION_SPEED
        if keys[pygame.K_d]:
            rotation_z -= ROTATION_SPEED
        
        pygame.display.flip()
        clock.tick(60) # 60 FPS
    
    pygame.quit()

if __name__ == "__main__":
    main()
