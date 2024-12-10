import random
import os

# Constants for the game
BOARD_SIZE = 7
EMPTY_CELL = '·'
MISS = 'O'
HIT = 'X'
SUNK = '#'

# Ship definitions
SHIPS = {
    3: 1,  # 1 ship of size 3
    2: 2,  # 2 ships of size 2
    1: 4   # 4 ships of size 1
}

# Helper to clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Convert letter coordinates to indices
def parse_coordinates(input_coord):
    try:
        letter, number = input_coord.upper()[0], int(input_coord[1:])
        row = ord(letter) - ord('A')
        col = number - 1
        if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
            return row, col
    except (IndexError, ValueError):
        pass
    return None

# Display the board
def display_board(board, reveal=False):
    clear_screen()
    header = "  " + " ".join(str(i + 1) for i in range(BOARD_SIZE))
    print(header)
    for i, row in enumerate(board):
        row_content = " ".join(
            cell if reveal or cell in {EMPTY_CELL, MISS, HIT, SUNK} else EMPTY_CELL 
            for cell in row
        )
        print(f"{chr(ord('A') + i)} {row_content}")

# Place ships on the board
def place_ships():
    board = [[EMPTY_CELL for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    for size, count in SHIPS.items():
        for _ in range(count):
            while True:
                orientation = random.choice(['H', 'V'])
                start_row = random.randint(0, BOARD_SIZE - 1)
                start_col = random.randint(0, BOARD_SIZE - 1)
                if can_place_ship(board, start_row, start_col, size, orientation):
                    place_ship(board, start_row, start_col, size, orientation)
                    break
    return board

# Check if a ship can be placed
def can_place_ship(board, row, col, size, orientation):
    for i in range(size):
        r = row + i if orientation == 'V' else row
        c = col + i if orientation == 'H' else col
        if not (0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE) or board[r][c] != EMPTY_CELL:
            return False
        # Check surroundings
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE and board[nr][nc] != EMPTY_CELL:
                    return False
    return True

# Place a ship on the board
def place_ship(board, row, col, size, orientation):
    for i in range(size):
        r = row + i if orientation == 'V' else row
        c = col + i if orientation == 'H' else col
        board[r][c] = str(size)

# Check for a hit
def check_hit(board, row, col):
    return board[row][col] not in {EMPTY_CELL, MISS, HIT, SUNK}

# Mark a ship as sunk
def mark_sunk(board, row, col, size):
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if board[r][c] == str(size):
                board[r][c] = SUNK

# Check if a ship is fully sunk
def is_sunk(board, row, col):
    size = board[row][col]
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if board[r][c] == size:
                return False
    return True

# Play the game
def play_game():
    player_name = input("Enter your name: ").strip()
    board = place_ships()
    display_board([[EMPTY_CELL for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)])
    visible_board = [[EMPTY_CELL for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    shots = 0

    while any(cell.isdigit() for row in board for cell in row):
        display_board(visible_board)
        shot = input("Enter your shot (e.g., A1): ").strip()
        coordinates = parse_coordinates(shot)

        if not coordinates:
            print("Invalid input. Try again.")
            continue

        row, col = coordinates
        if visible_board[row][col] != EMPTY_CELL:
            print("You already shot there. Try again.")
            continue

        shots += 1
        if check_hit(board, row, col):
            size = board[row][col]
            board[row][col] = HIT
            visible_board[row][col] = HIT
            if is_sunk(board, row, col):
                mark_sunk(board, row, col, size)
                visible_board = [[cell if cell != HIT else SUNK for cell in row] for row in visible_board]
                print("You sunk a ship!")
        else:
            board[row][col] = MISS
            visible_board[row][col] = MISS
            print("Miss!")

    display_board(visible_board, reveal=True)
    print(f"Congratulations {player_name}! You won in {shots} shots.")

    return player_name, shots

# Leaderboard management
def show_leaderboard(players):
    players = sorted(players, key=lambda x: x[1])
    print("\nLEADERBOARD:")
    for i, (name, shots) in enumerate(players, 1):
        print(f"{i}. {name} - {shots} shots")

# Main game loop
def main():
    players = []
    while True:
        player_name, shots = play_game()
        players.append((player_name, shots))
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != 'yes':
            show_leaderboard(players)
            break

if __name__ == "__main__":
    main()
