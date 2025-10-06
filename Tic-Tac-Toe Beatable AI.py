import sys
import pygame
import numpy as np
import random

pygame.init()

# Colours
WHITE = (255, 255, 255)
GREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Board dimensions
WIDTH = 500
HEIGHT = 500
LINE_WIDTH = 5
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
screen.fill(BLACK)

board = np.zeros((BOARD_ROWS, BOARD_COLS))


def draw_lines(color=WHITE):
    for i in range(1, BOARD_ROWS):
        # Horizontal
        pygame.draw.line(screen, color, (0, SQUARE_SIZE * i), (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
        # Vertical
        pygame.draw.line(screen, color, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)


def draw_figures(color=WHITE):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, color,
                                   (int(col * SQUARE_SIZE + SQUARE_SIZE // 2),
                                    int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, color,(col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4),(col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4),CROSS_WIDTH)
                pygame.draw.line(screen, color,(col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4),(col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4),CROSS_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0


def is_board_full(check_board=board):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if check_board[row][col] == 0:
                return False
    return True


def check_win(player, check_board=board):
    # Rows
    for row in range(BOARD_ROWS):
        if check_board[row][0] == player and check_board[row][1] == player and check_board[row][2] == player:
            return True
    # Columns
    for col in range(BOARD_COLS):
        if check_board[0][col] == player and check_board[1][col] == player and check_board[2][col] == player:
            return True
    # Main diagonal
    if check_board[0][0] == player and check_board[1][1] == player and check_board[2][2] == player:
        return True
    # Anti-diagonal
    if check_board[0][2] == player and check_board[1][1] == player and check_board[2][0] == player:
        return True
    return False


# ---------------- Beatable AI ----------------
def best_move():
    # 1. Win if possible
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                board[row][col] = 2
                if check_win(2):
                    return True
                board[row][col] = 0

    # 2. Block player if they can win
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                board[row][col] = 1
                if check_win(1):
                    board[row][col] = 2
                    return True
                board[row][col] = 0

    # 3. Take center if free
    if board[1][1] == 0:
        board[1][1] = 2
        return True

    # 4. Take a random corner if free
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    random.shuffle(corners)
    for row, col in corners:
        if board[row][col] == 0:
            board[row][col] = 2
            return True

    # 5. Take any random available spot
    empty = [(r, c) for r in range(BOARD_ROWS) for c in range(BOARD_COLS) if board[r][c] == 0]
    if empty:
        row, col = random.choice(empty)
        board[row][col] = 2
        return True

    return False


def restart_game():
    screen.fill(BLACK)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0


draw_lines()

game_over = False

# ------------------ Main Event Loop ------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            row = event.pos[1] // SQUARE_SIZE
            col = event.pos[0] // SQUARE_SIZE

            if available_square(row, col):
                # Player move
                mark_square(row, col, 1)
                if check_win(1):
                    game_over = True
                else:
                    # AI move
                    if not is_board_full():
                        best_move()
                        if check_win(2):
                            game_over = True

                # Check draw
                if not game_over and is_board_full():
                    game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()
                game_over = False

    # Draw board & pieces
    draw_figures()
    if game_over:
        if check_win(1):
            draw_figures(GREEN)
            draw_lines(GREEN)
        elif check_win(2):
            draw_figures(RED)
            draw_lines(RED)
        else:
            draw_figures(GREY)
            draw_lines(GREY)

    pygame.display.update()


