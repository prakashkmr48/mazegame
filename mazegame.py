import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Simple Maze Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player properties
player_size = 20
player_x = 50
player_y = 50

# Maze properties
maze = [
    "#############",
    "#P          #",
    "#           #",
    "#           #",
    "#           #",
    "#           #",
    "#           #",
    "#           #",
    "#############"
]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_y -= player_size
            elif event.key == pygame.K_DOWN:
                player_y += player_size
            elif event.key == pygame.K_LEFT:
                player_x -= player_size
            elif event.key == pygame.K_RIGHT:
                player_x += player_size

    # Check for collisions with maze walls
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == "#":
                wall_rect = pygame.Rect(col * player_size, row * player_size, player_size, player_size)
                if player_rect.colliderect(wall_rect):
                    player_x, player_y = 50, 50  # Reset player position

    # Clear the screen
    screen.fill(WHITE)

    # Draw maze
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == "#":
                pygame.draw.rect(screen, BLACK, (col * player_size, row * player_size, player_size, player_size))

    # Draw player
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
