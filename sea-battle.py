import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_board(size=7):
    return [[" " for _ in range(size)] for _ in range(size)]

def display_board(board, reveal=False):
    print("  " + " ".join("ABCDEFG"[i] for i in range(len(board))))
    for i, row in enumerate(board):
        print(f"{i+1} " + " ".join(cell if reveal or cell in ("M", "H", "X") else "." for cell in row))

def place_ships(board):
    for size in [3, 2, 2, 1, 1, 1, 1]:
        while True:
            orientation = random.choice(["H", "V"])
            row, col = random.randint(0, 6), random.randint(0, 6)
            if can_place_ship(board, row, col, size, orientation):
                for i in range(size):
                    if orientation == "H":
                        board[row][col + i] = "S"
                    else:
                        board[row + i][col] = "S"
                break

def can_place_ship(board, row, col, size, orientation):
    for i in range(size):
        r, c = (row, col + i) if orientation == "H" else (row + i, col)
        if not (0 <= r < 7 and 0 <= c < 7) or board[r][c] != " ":
            return False
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if 0 <= r + dr < 7 and 0 <= c + dc < 7 and board[r + dr][c + dc] == "S":
                    return False
    return True

def process_shot(board, player_board, row, col):
    if board[row][col] == "S":
        board[row][col] = player_board[row][col] = "H"
        if is_ship_sunk(board, row, col):
            mark_sunk_ship(board, player_board, row, col)
            return "victory" if all_ships_sunk(board) else "sunk"
        return "hit"
    elif board[row][col] == " ":
        board[row][col] = player_board[row][col] = "M"
        return "miss"
    return "already"

def is_ship_sunk(board, row, col):
    stack = [(row, col)]
    visited = set()
    while stack:
        r, c = stack.pop()
        if (r, c) in visited or board[r][c] != "H":
            continue
        visited.add((r, c))
        for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < 7 and 0 <= nc < 7:
                stack.append((nr, nc))
    for r, c in visited:
        for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < 7 and 0 <= nc < 7 and board[nr][nc] == "S":
                return False
    return True

def mark_sunk_ship(board, player_board, row, col):
    stack = [(row, col)]
    while stack:
        r, c = stack.pop()
        if board[r][c] == "H":
            board[r][c] = player_board[r][c] = "X"
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < 7 and 0 <= nc < 7:
                    stack.append((nr, nc))

def all_ships_sunk(board):
    return not any("S" in row for row in board)

def parse_coordinates(coords):
    return "ABCDEFG".index(coords[0].upper()), int(coords[1]) - 1

def play_game(player_name, leaderboard):
    board, player_board = create_board(), create_board()
    place_ships(board)
    shots = 0
    while True:
        clear_screen()
        print(f"Игрок: {player_name} | Выстрелы: {shots}")
        display_board(player_board)
        coords = input("Введите координаты (например, A1): ")
        try:
            row, col = parse_coordinates(coords)
            result = process_shot(board, player_board, row, col)
            clear_screen()
            display_board(player_board)
            if result == "hit":
                print("Попадание!")
            elif result == "sunk":
                print("Корабль потоплен!")
            elif result == "miss":
                print("Мимо!")
            elif result == "victory":
                print(f"Победа! Вы потопили все корабли за {shots + 1} выстрелов.")
                leaderboard[player_name] = shots + 1
                break
            else:
                print("Уже стреляли сюда!")
            shots += 1
        except (ValueError, IndexError):
            print("Неверные координаты. Попробуйте ещё раз.")

if __name__ == "__main__":
    leaderboard = {}
    while True:
        clear_screen()
        player_name = input("Введите ваше имя: ")
        play_game(player_name, leaderboard)
        if input("Сыграть ещё раз? (y/n): ").lower() != "y":
            break
    clear_screen()
    print("Рейтинг игроков:")
    for name, shots in sorted(leaderboard.items(), key=lambda x: x[1]):
        print(f"{name}: {shots} выстрелов")

