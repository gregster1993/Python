import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen size and colors
WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tron Game")

# Game speed
clock = pygame.time.Clock()
FPS = 15

# Light cycle attributes
CYCLE_SIZE = 10
DIRECTIONS = {
    'UP': (0, -CYCLE_SIZE),
    'DOWN': (0, CYCLE_SIZE),
    'LEFT': (-CYCLE_SIZE, 0),
    'RIGHT': (CYCLE_SIZE, 0)
}

# Player classes
class LightCycle:
    def __init__(self, color, start_pos, start_direction):
        self.color = color
        self.positions = [start_pos]
        self.direction = start_direction
        self.alive = True
    
    def move(self):
        if not self.alive:
            return
        new_position = (
            self.positions[-1][0] + self.direction[0],
            self.positions[-1][1] + self.direction[1]
        )
        self.positions.append(new_position)
    
    def change_direction(self, direction):
        # Prevent reversing back into the previous segment
        if (direction[0] != -self.direction[0] or 
            direction[1] != -self.direction[1]):
            self.direction = direction
    
    def draw(self):
        for pos in self.positions:
            pygame.draw.rect(screen, self.color, (*pos, CYCLE_SIZE, CYCLE_SIZE))
    
    def check_collisions(self, other_positions):
        # Check if the light cycle has hit a wall
        head_x, head_y = self.positions[-1]
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            self.alive = False
        # Check if the light cycle has hit itself or the opponent
        if self.positions[-1] in self.positions[:-1] or self.positions[-1] in other_positions:
            self.alive = False

# Initialize players
player1 = LightCycle(BLUE, (100, HEIGHT // 2), DIRECTIONS['RIGHT'])
player2 = LightCycle(RED, (WIDTH - 100, HEIGHT // 2), DIRECTIONS['LEFT'])

# Main game loop
while True:
    screen.fill(BLACK)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Player 1 controls (WASD)
            if event.key == pygame.K_w:
                player1.change_direction(DIRECTIONS['UP'])
            elif event.key == pygame.K_s:
                player1.change_direction(DIRECTIONS['DOWN'])
            elif event.key == pygame.K_a:
                player1.change_direction(DIRECTIONS['LEFT'])
            elif event.key == pygame.K_d:
                player1.change_direction(DIRECTIONS['RIGHT'])
            # Player 2 controls (Arrow keys)
            elif event.key == pygame.K_UP:
                player2.change_direction(DIRECTIONS['UP'])
            elif event.key == pygame.K_DOWN:
                player2.change_direction(DIRECTIONS['DOWN'])
            elif event.key == pygame.K_LEFT:
                player2.change_direction(DIRECTIONS['LEFT'])
            elif event.key == pygame.K_RIGHT:
                player2.change_direction(DIRECTIONS['RIGHT'])
    
    # Move players
    player1.move()
    player2.move()
    
    # Check collisions
    player1.check_collisions(player2.positions)
    player2.check_collisions(player1.positions)
    
    # Draw players
    player1.draw()
    player2.draw()
    
    # End game if a player is not alive
    if not player1.alive or not player2.alive:
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)
