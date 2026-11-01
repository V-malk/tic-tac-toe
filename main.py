import tkinter as tk
from tkinter import messagebox

board = [" " for _ in range(9)]
current_player = "X"
buttons = []
status_label = None

def is_valid_move(index):
    if board[index] != " ":
        return False
    return True

def check_win(player):
    win_combos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for combo in win_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def check_draw():
    return " " not in board

# Ветка 5: Новая игра
def reset_game():
    global board, current_player
    board = [" " for _ in range(9)]
    current_player = "X"
    for btn in buttons:
        btn.config(text=" ", state="normal")
    status_label.config(text=f"Ход игрока: {current_player}")

def play_turn(index):
    global current_player
    if not is_valid_move(index):
        return
    
    board[index] = current_player
    buttons[index].config(text=current_player, state="disabled", disabledforeground="black")
    
    if check_win(current_player):
        messagebox.showinfo("Победа!", f"Победитель: {current_player}")
        reset_game()
        return
        
    if check_draw():
        messagebox.showinfo("Ничья!", "Победителя нет.")
        reset_game()
        return
        
    current_player = "O" if current_player == "X" else "X"
    status_label.config(text=f"Ход игрока: {current_player}")

def create_gui():
    global status_label
    root = tk.Tk()
    root.title("Крестики-нолики")
    
    frame = tk.Frame(root)
    frame.pack(pady=10)
    
    for i in range(9):
        btn = tk.Button(frame, text=" ", width=4, height=2, font=("Arial", 16), command=lambda i=i: play_turn(i))
        row, col = i // 3, i % 3
        btn.grid(row=row, column=col, padx=2, pady=2)
        buttons.append(btn)
        
    status_label = tk.Label(root, text=f"Ход игрока: {current_player}", font=("Arial", 12))
    status_label.pack(pady=5)
    
    restart_btn = tk.Button(root, text="Новая игра", command=reset_game, font=("Arial", 12))
    restart_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()