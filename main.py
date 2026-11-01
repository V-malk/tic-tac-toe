import tkinter as tk
from tkinter import messagebox

board = [" " for _ in range(9)]
current_player = "X"
buttons = []

def is_valid_move(index):
    if board[index] != " ":
        return False
    return True

# Ветка 2: Правила игры
def play_turn(index):
    global current_player
    if not is_valid_move(index):
        return
    
    board[index] = current_player
    buttons[index].config(text=current_player, state="disabled", disabledforeground="black")
    
    # Смена игрока (по очереди)
    current_player = "O" if current_player == "X" else "X"

def create_gui():
    root = tk.Tk()
    root.title("Крестики-нолики")
    frame = tk.Frame(root)
    frame.pack(pady=10)
    
    for i in range(9):
        btn = tk.Button(frame, text=" ", width=4, height=2, command=lambda i=i: play_turn(i))
        row, col = i // 3, i % 3
        btn.grid(row=row, column=col, padx=2, pady=2)
        buttons.append(btn)
    root.mainloop()

if __name__ == "__main__":
    create_gui()