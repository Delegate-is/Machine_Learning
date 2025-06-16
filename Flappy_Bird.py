import pygame
import sys
import random

# 1. Initialize Pygame
pygame.init()

# 2. Game Constants and Variables
SCREEN_WIDTH = 448 # Typical Flappy Bird game width
SCREEN_HEIGHT = 600 # Adjusted height to fit floor and content
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# Game State Variables
game_active = True # True when the game is being played, False on game over
score = 0
high_score = 0

# Bird Physics
gravity = 0.25 # How fast the bird falls
bird_movement = 0 # Current vertical speed of the bird

# Floor Movement
floor_x_pos = 0 # X position for the repeating floor image

# Pipe List to store all active pipe rectangles
pipe_list = []

# Possible Y heights for the gap between pipes (where the bottom pipe starts)
pipe_height = [200, 250, 300, 350, 400]

# 3. Load Game Assets
# IMPORTANT: You need to create an 'assets' folder in the same directory as this script
# and place your image files there.
# Placeholder images - replace with your actual game assets!

try:
    # Background image (scale to screen size)
    bg_img = pygame.image.load('assets/background.png').convert()
    bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Floor image (scale to screen width)
    floor_img = pygame.image.load('assets/floor.png').convert_alpha()
    floor_img = pygame.transform.scale(floor_img, (SCREEN_WIDTH, floor_img.get_height()))

    # Bird images for animation
    bird_downflap = pygame.image.load('assets/bird_down.png').convert_alpha()
    bird_midflap = pygame.image.load('assets/bird_mid.png').convert_alpha()
    bird_upflap = pygame.image.load('assets/bird_up.png').convert_alpha()
    bird_frames = [bird_downflap, bird_midflap, bird_upflap]
    bird_index = 0
    # Start with the first bird frame and create its rect
    bird_img = bird_frames[bird_index]
    bird_rect = bird_img.get_rect(center=(50, SCREEN_HEIGHT // 2))

    # Pipe image
    pipe_img = pygame.image.load('assets/pipe.png').convert_alpha()
    # Scale pipe height, width can be original or adjusted as needed
    pipe_img = pygame.transform.scale(pipe_img, (pipe_img.get_width(), 300)) # Example scaling

    # Game Over image (optional)
    game_over_img = pygame.image.load('assets/game_over.png').convert_alpha()
    game_over_img = pygame.transform.scale(game_over_img, (game_over_img.get_width() * 0.8, game_over_img.get_height() * 0.8))


except pygame.error as e:
    print(f"Error loading asset: {e}. Make sure you have an 'assets' folder with images like 'background.png', 'floor.png', 'bird_down.png', 'bird_mid.png', 'bird_up.png', 'pipe.png', 'game_over.png'.")
    pygame.quit()
    sys.exit()

# Fonts for displaying score/text
game_font = pygame.font.Font('freesansbold.ttf', 30) # Default Pygame font, size 30

# Sound Effects (Uncomment and provide sound files if you want them)
# try:
#     flap_sound = pygame.mixer.Sound('assets/sfx_wing.wav')
#     hit_sound = pygame.mixer.Sound('assets/sfx_hit.wav')
#     score_sound = pygame.mixer.Sound('assets/sfx_point.wav')
# except pygame.error as e:
#     print(f"Error loading sound effect: {e}. Sound effects will not play.")


# Custom Events for Timers
# Event to spawn pipes regularly
PIPE_SPAWN = pygame.USEREVENT
pygame.time.set_timer(PIPE_SPAWN, 1200) # Trigger PIPE_SPAWN event every 1200 milliseconds (1.2 seconds)

# Event for bird flapping animation
BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200) # Trigger BIRDFLAP event every 200 milliseconds

# 4. Game Functions

def draw_floor():
    """Draws the moving floor image twice to create a continuous loop."""
    # Draw first floor image
    screen.blit(floor_img, (floor_x_pos, SCREEN_HEIGHT - floor_img.get_height()))
    # Draw second floor image right after the first to create the loop effect
    screen.blit(floor_img, (floor_x_pos + SCREEN_WIDTH, SCREEN_HEIGHT - floor_img.get_height()))

def create_pipe():
    """Creates a new top and bottom pipe rectangle pair at a random height."""
    # Choose a random y position for the bottom pipe's top edge
    random_pipe_pos = random.choice(pipe_height)

    # Create the bottom pipe rectangle
    # Starts off-screen to the right (SCREEN_WIDTH + 50)
    bottom_pipe = pipe_img.get_rect(midtop=(SCREEN_WIDTH + 50, random_pipe_pos))

    # Create the top pipe rectangle
    # The gap height is 150 pixels between the bottom of the top pipe and top of the bottom pipe
    top_pipe = pipe_img.get_rect(midbottom=(SCREEN_WIDTH + 50, random_pipe_pos - 150))
    return bottom_pipe, top_pipe # Return both pipe rectangles

def move_pipes(pipes):
    """Moves all pipes in the list to the left."""
    for pipe in pipes:
        pipe.centerx -= 3 # Move pipes 3 pixels to the left each frame (pipe speed)
    # Filter out pipes that have moved completely off-screen to the left
    return [pipe for pipe in pipes if pipe.right > -50] # Keep pipes that are still visible or just slightly off

def draw_pipes(pipes):
    """Draws all pipes in the list on the screen."""
    for pipe in pipes:
        if pipe.bottom >= SCREEN_HEIGHT: # This is a bottom pipe (its bottom is at or below screen height)
            screen.blit(pipe_img, pipe)
        else: # This is a top pipe (its bottom is above screen height, needs to be flipped)
            # Flip the pipe image vertically for the top pipe
            flipped_pipe = pygame.transform.flip(pipe_img, False, True)
            screen.blit(flipped_pipe, pipe)

def bird_animation_update():
    """Updates the bird's image for flapping animation."""
    new_bird = bird_frames[bird_index].get_rect(center = (50, bird_rect.centery))
    return new_bird

def check_collision(pipes):
    """
    Checks for collision between the bird and any pipes, or the floor/ceiling.
    Returns False if collision detected (game over), True otherwise.
    """
    global game_active # Declare intention to modify the global game_active variable

    # Check collision with pipes
    for pipe in pipes:
        if bird_rect.colliderect(pipe): # Check if bird's rectangle overlaps with pipe's rectangle
            # try:
            #     hit_sound.play() # Play hit sound
            # except:
            #     pass
            game_active = False # Set game state to game over
            return False

    # Check collision with floor
    if bird_rect.bottom >= SCREEN_HEIGHT - floor_img.get_height():
        # try:
        #     hit_sound.play() # Play hit sound
        # except:
        #     pass
        game_active = False
        return False

    # Check collision with top of the screen (bird flying too high)
    if bird_rect.top <= 0:
        # try:
        #     hit_sound.play() # Play hit sound
        # except:
        #     pass
        game_active = False
        return False

    return True # No collision detected

def display_score(game_state):
    """Displays the current score and high score on the screen."""
    if game_state == 'main_game':
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255)) # Render current score in white
        score_rect = score_surface.get_rect(center=(SCREEN_WIDTH // 2, 50)) # Position at top center
        screen.blit(score_surface, score_rect)
    elif game_state == 'game_over':
        # Display current score
        score_surface = game_font.render(f'Score: {int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))
        screen.blit(score_surface, score_rect)

        # Display high score
        high_score_surface = game_font.render(f'High Score: {int(high_score)}', True, (255, 255, 255))
        # Position high score below current score, slightly above the game over message
        high_score_rect = high_score_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))
        screen.blit(high_score_surface, high_score_rect)

def update_high_score(current_score, highscore):
    """Updates the high score if the current score is greater."""
    if current_score > highscore:
        highscore = current_score
    return highscore

def draw_game_over_message():
    """Draws the 'Game Over' image or text on the screen."""
    # You can choose to blit an image or render text
    # Option 1: Image
    game_over_rect = game_over_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(game_over_img, game_over_rect)

    # Option 2: Text (if you don't have an image)
    # game_over_text = game_font.render("GAME OVER", True, (255, 0, 0)) # Red text
    # game_over_text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    # screen.blit(game_over_text, game_over_text_rect)

# 5. Game Loop
running = True # Flag to keep the game running

while running:
    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # User clicks the close button
            running = False # Stop the game loop
            pygame.quit()   # Uninitialize pygame modules
            sys.exit()      # Exit the program

        if event.type == pygame.KEYDOWN: # A key is pressed down
            if event.key == pygame.K_SPACE: # If the spacebar is pressed
                if game_active:
                    bird_movement = 0      # Reset vertical movement
                    bird_movement -= 6     # Make the bird jump up
                    # try:
                    #     flap_sound.play() # Play flap sound
                    # except:
                    #     pass
                else: # If game is over and space is pressed, reset the game
                    game_active = True
                    pipe_list.clear()      # Clear all pipes
                    bird_rect.center = (50, SCREEN_HEIGHT // 2) # Reset bird position
                    bird_movement = 0      # Reset bird movement
                    score = 0              # Reset score

        if event.type == PIPE_SPAWN: # Custom event for spawning pipes
            if game_active: # Only spawn pipes if the game is active
                pipe_list.extend(create_pipe()) # Add new pipe pair to the list

        if event.type == BIRDFLAP: # Custom event for bird animation
            bird_index = (bird_index + 1) % len(bird_frames) # Cycle through bird frames
            bird_img = bird_frames[bird_index] # Update current bird image
            bird_rect = bird_animation_update() # Update bird's rect based on new image size/center


    # --- Game Logic ---
    if game_active:
        # Apply gravity to bird
        bird_movement += gravity
        bird_rect.centery += bird_movement # Move bird by its current vertical movement

        # Move and draw pipes
        pipe_list = move_pipes(pipe_list) # Update pipe positions and remove old pipes
        # draw_pipes(pipe_list) # This is drawn below after background

        # Move floor
        floor_x_pos -= 1 # Move floor to the left
        if floor_x_pos <= -SCREEN_WIDTH: # If floor moves off-screen, reset its position
            floor_x_pos = 0

        # Check for collisions
        game_active = check_collision(pipe_list) # Update game_active based on collision

        # Scoring Logic: check if bird has passed a pipe
        for pipe in pipe_list:
            # Check if the bird has passed the pipe (bird's right edge passed pipe's left edge)
            # and ensure we only score once per pipe pair (e.g., check a specific x-range)
            if 49 < pipe.centerx < 51 and game_active: # Arbitrary small range near bird's x-pos
                score += 0.5 # Add 0.5 because each pipe pair consists of two rectangles
                # try:
                #     score_sound.play() # Play score sound
                # except:
                #     pass
                break # Only score once per pipe pair to avoid double counting


    # --- Drawing Elements ---
    screen.blit(bg_img, (0, 0)) # Draw background first
    draw_pipes(pipe_list)       # Draw pipes (behind bird and floor)
    screen.blit(bird_img, bird_rect) # Draw bird
    draw_floor()                # Draw floor (on top of other elements)

    # Display Score
    if game_active:
        display_score('main_game')
    else:
        high_score = update_high_score(score, high_score) # Update high score when game ends
        draw_game_over_message() # Display "GAME OVER" message/image
        display_score('game_over') # Display final score and high score

    # --- Update Display and Control Frame Rate ---
    pygame.display.update() # Update the entire screen
    clock.tick(120)         # Limit the game to 120 frames per second (FPS)
