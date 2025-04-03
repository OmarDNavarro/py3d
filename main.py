# main.py

import pygame
import numpy as np

import transformation
import shape
import constants
import rendering


def main():

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    clock = pygame.time.Clock()
    
    """Main loop for rendering the cube."""
    running = True

    objects = list()
    for i in range(9):
        objects.append(shape.tetrahedron((i * 4, 5, 0)))
        objects.append(shape.cube((i*4, 0, 0)))
        objects.append(shape.pyramid((i*4, -5, 0)))

    # Define camera position (starting at origin)
    camera_pos = np.array([15.0, 0.0, -20.0])  # Start at x at 15 and z = -20 to see all objects

    rotation_x, rotation_y, rotation_z = 0, 0, 0

    while running:
        screen.fill(constants.BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get user input for rotations
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            camera_pos[2] += constants.CAMERA_SPEED
        if keys[pygame.K_s]:
            camera_pos[2] -= constants.CAMERA_SPEED

        if keys[pygame.K_a]:
            camera_pos[0] -= constants.CAMERA_SPEED
        if keys[pygame.K_d]: 
            camera_pos[0] += constants.CAMERA_SPEED

        if keys[pygame.K_q]:
            camera_pos[1] -= constants.CAMERA_SPEED
        if keys[pygame.K_e]: 
            camera_pos[1] += constants.CAMERA_SPEED

        rotation_x += constants.ROTATION_SPEED
        rotation_y += constants.ROTATION_SPEED
        rotation_z += constants.ROTATION_SPEED

        # Wrap the angles to keep them in the range [0, 2π]
        rotation_x %= constants.MAX_ROTATION
        rotation_y %= constants.MAX_ROTATION
        rotation_z %= constants.MAX_ROTATION

        # Apply rotations to each object
        for object in objects:
            vertices, edges, position = object
            
            # Apply rotation in order X -> Y
            rotated_vertices = transformation.rotate_x(vertices, rotation_x)
            rotated_vertices = transformation.rotate_y(rotated_vertices, rotation_y)

            # Create the transformed object with rotated vertices
            transformed_object = (rotated_vertices, edges, position)

            # Draw the transformed object
            rendering.draw_object(transformed_object, camera_pos, screen)
        
        pygame.display.flip()
        clock.tick(60) # 60 FPS
    
    pygame.quit()

if __name__ == "__main__":
    main()
