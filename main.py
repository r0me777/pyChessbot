import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 700, 700
chessboard = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chess Board")

# Define colors
white = 'brown'  # Brown -> Just looks nice tbh
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
    'K': 'pink',   # White king
    'p': 'black',  # Black pawn
    'r': 'black',  # Black rook
    'n': 'black',  # Black knight
    'b': 'black',  # Black bishop
    'q': 'black',  # Black queen
    'k': 'pink',   # Black king
}

# Initial chessboard layout with multiple arrays
chessboard_layout_text = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
]

#Helper function to convert text layout to a 2D array (will probably turn into object based arry)
def text_to_board(text_layout):
    return [list(row) for row in text_layout]

# Helper function to convert a 2D array to text layout, (again will probably turn into object based arry)
def board_to_text(board):
    return [''.join(row) for row in board]

#Function to draw the chessboard and pieces
def draw_board(board):
    for row in range(8): #Iterates through rows
        for col in range(8):
            color = white if (row + col) % 2 == 0 else black
            pygame.draw.rect(chessboard, color, (col * square_size, row * square_size, square_size, square_size))

            piece_code = board[row][col]
            if piece_code != ' ':
                piece_color = piece_colors[piece_code]
                pygame.draw.rect(chessboard, piece_color, (col * square_size + 15, row * square_size + 15, piece_size, piece_size))

# Initial setup
chessboard_layout = text_to_board(chessboard_layout_text)

# Main game loop
running = True
selected_piece = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Handle piece selection based on mouse click
            mouse_x, mouse_y = pygame.mouse.get_pos()
            col = mouse_x // square_size
            row = mouse_y // square_size
            selected_piece = (row, col)

        elif event.type == pygame.MOUSEBUTTONUP and selected_piece:
            #Handle piece movement based on mouse release
            new_mouse_x, new_mouse_y = pygame.mouse.get_pos()
            new_col = new_mouse_x // square_size
            new_row = new_mouse_y // square_size

            # Swap the selected piece with the piece in the new position (Probably won't work later)
            chessboard_layout[selected_piece[0]][selected_piece[1]], chessboard_layout[new_row][new_col] = \
                chessboard_layout[new_row][new_col], chessboard_layout[selected_piece[0]][selected_piece[1]]

            selected_piece = None  # Deselect the piece after moving ()

    #Draw the chessboard and pieces
    draw_board(chessboard_layout)

    # Highlight selected piece if any
    if selected_piece:
        row, col = selected_piece
        pygame.draw.rect(chessboard, (255, 255, 0), (col * square_size, row * square_size, square_size, square_size), 5)

    # Update the display
    pygame.display.flip()



print("Terminal Game")
for row in chessboard_layout: #Prints the ending text display, just so you see whats going on
    print(" ".join(row))

# Quit Pygame
pygame.quit()
sys.exit()
