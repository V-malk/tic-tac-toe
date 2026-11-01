import tkinter as tk
from tkinter import messagebox

board = [" " for _ in range(9)]
buttons = []

# Ветка 1: Проверка ввода
def is_valid_move(index):
    if board[index] != " ":
        messagebox.showwarning("Ошибка", "Клетка занята! Сходите еще раз.")
        return False
    return True

def create_gui():
    root = tk.Tk()
    root.title("Крестики-нолики")
    frame = tk.Frame(root)
    frame.pack(pady=10)
    
    for i in range(9):
        btn = tk.Button(frame, text=" ", width=4, height=2)
        row, col = i // 3, i % 3
        btn.grid(row=row, column=col, padx=2, pady=2)
        buttons.append(btn)
    root.mainloop()

if __name__ == "__main__":
    create_gui()