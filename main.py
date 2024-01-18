import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 700, 700
chessboard = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chess Board")



# Define colors
white = 'brown'  # Brown
black = 'beige'  # Beige

# Define the size of each square
square_size = width // 8
piece_size = square_size - 30  # Adjusted size for the pieces

# Create a dictionary to map chess piece codes to their respective colors
piece_colors = {
    'P': 'white',  # White pawn
    'R': 'white',  # White rook
    'N': 'white',  # White knight
    'B': 'white',  # White bishop
    'Q': 'white',  # White queen
    'K': 'pink',  # White king
    'p': 'black',  # Black pawn
    'r': 'black',  # Black rook
    'n': 'black',  # Black knight
    'b': 'black',  # Black bishop
    'q': 'black',  # Black queen
    'k': 'pink',  # Black king
}

# Example chessboard layout (you can modify this based on your initial positions)
chessboard_layout = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
]

# Draw the chessboard squares on the chessboard surface
for row in range(8):
    for col in range(8):
        color = white if (row + col) % 2 == 0 else black
        pygame.draw.rect(chessboard, color, (col * square_size, row * square_size, square_size, square_size))

# Load chess piece rectangles onto the chessboard surface
for row in range(8):
    for col in range(8):
        piece_code = chessboard_layout[row][col]
        if piece_code != ' ':
            piece_color = piece_colors[piece_code]
            pygame.draw.rect(chessboard, piece_color, (col * square_size + 15, row * square_size + 15, piece_size, piece_size))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the chessboard on the main screen

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()


