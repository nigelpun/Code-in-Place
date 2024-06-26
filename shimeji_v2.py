<<<<<<< HEAD
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Basic Shimeji")

# Load images
standing = pygame.image.load("standing.png")
clicked = pygame.image.load("clicked.png")

# Set initial position and state
x = random.randint(0, width - standing.get_width())
y = height - standing.get_height()
is_clicked = False
click_time = 0

# Set up the clock
clock = pygame.time.Clock()

# Set up movement timer
move_timer = 0
move_interval = random.randint(2000, 6000)  # 2-6 seconds in milliseconds

# Main game loop
running = True
while running:
    current_time = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if standing.get_rect(topleft=(x, y)).collidepoint(event.pos):
                is_clicked = True
                click_time = current_time

    # Check if 2 seconds have passed since the click
    if is_clicked and current_time - click_time > 2000:
        is_clicked = False

    # Move the shimeji
    if current_time - move_timer > move_interval:
        move_direction = random.choice([-1, 1])  # -1 for left, 1 for right
        move_distance = random.randint(50, 100)  # pixels to move
        
        # Calculate new position
        new_x = x + (move_direction * move_distance)
        
        # Ensure the shimeji stays within the screen bounds
        new_x = max(0, min(new_x, width - standing.get_width()))
        
        x = new_x
        move_timer = current_time
        move_interval = random.randint(2000, 6000)

    # Clear the screen
    screen.fill((255, 255, 255))  # White background

    # Draw the shimeji
    if is_clicked:
        screen.blit(clicked, (x, y))
    else:
        screen.blit(standing, (x, y))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
=======
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Basic Shimeji")

# Load images
standing = pygame.image.load("standing.png")
clicked = pygame.image.load("clicked.png")

# Set initial position and state
x = random.randint(0, width - standing.get_width())
y = height - standing.get_height()
is_clicked = False
click_time = 0

# Set up the clock
clock = pygame.time.Clock()

# Set up movement timer
move_timer = 0
move_interval = random.randint(2000, 6000)  # 2-6 seconds in milliseconds

# Main game loop
running = True
while running:
    current_time = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if standing.get_rect(topleft=(x, y)).collidepoint(event.pos):
                is_clicked = True
                click_time = current_time

    # Check if 2 seconds have passed since the click
    if is_clicked and current_time - click_time > 2000:
        is_clicked = False

    # Move the shimeji
    if current_time - move_timer > move_interval:
        move_direction = random.choice([-1, 1])  # -1 for left, 1 for right
        move_distance = random.randint(50, 100)  # pixels to move
        
        # Calculate new position
        new_x = x + (move_direction * move_distance)
        
        # Ensure the shimeji stays within the screen bounds
        new_x = max(0, min(new_x, width - standing.get_width()))
        
        x = new_x
        move_timer = current_time
        move_interval = random.randint(2000, 6000)

    # Clear the screen
    screen.fill((255, 255, 255))  # White background

    # Draw the shimeji
    if is_clicked:
        screen.blit(clicked, (x, y))
    else:
        screen.blit(standing, (x, y))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
>>>>>>> 14809f9b4a964269741085c6e6dd87c9e629c3bf
pygame.quit()