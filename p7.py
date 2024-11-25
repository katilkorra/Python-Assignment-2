# tic tac toe game
# def print_board(board):
#     print("--------------")
#     for i in range(3):
#         print("|" ,end = " ")
#         for j in range(3):
#             print(board[i][j], "|", end = " ")
#         print()
#         print("---------------")


# def check_win(board,player):
#     for i in range(3):
#         if board[i][0] == board[i][1] == board[i][2] == player:
#             return True
#         if board[0][i] == board[1][i] == board[2][i] == player:
#             return True
#     if board[0][0] == board[1][1] == board[2][2] == player:
#             return True
#     if board[0][2] == board[1][1] == board[2][0] == player:
#             return True
#     return False

# def tic_toc_toe():
#      board =[["","",""],["","",""],["","",""]]
#      current_player = "X"
#      while True:
#           print_board(board)
#           row = int(input(f"{current_player}, choose your row (0 to 2)"))
#           col = int(input(f"{current_player}, choose your col (0 to 2)"))
#           if row < 0 or row > 2 or col < 0 or col > 2:
#                 print("Invalid input. Please enter a number between 0 and 2.")
                    
#           if board[row][col] != "":
#                print("The spot is already taken")
#                continue
#           board[row][col] = current_player
#           if check_win(board,current_player):
#                print_board(board)
#                print(f"{current_player} wins :")
#                break
#           if all("" not in row for row in board):
#                 print_board(board)
#                 print("Game is tie now")
#                 break
#           current_player = "0" if current_player=="X" else "X"
          

# tic_toc_toe()




# using packages

import tkinter as tk   #standard Python interface to the Tk GUI toolkit. 
                        # It provides tools to create windows, buttons, 
                        #   and other GUI elements.
from tkinter import messagebox #This module from tkinter is used to 
                                 #show message boxes for alerts,
                                 #confirmations, and information.

class TicTacToe:
    def __init__(self):    #This is the constructor method that initializes 
                            #the game when an instance of the class is created.
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("262x260")
        self.player_turn = "X"

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, command=lambda row=i, column=j: self.click(row, column), height=5, width=11)
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def click(self, row, column):
        if self.buttons[row][column]['text'] == "":
            self.buttons[row][column]['text'] = self.player_turn
            if self.check_win():
                messagebox.showinfo("Game Over", f"Player {self.player_turn} wins!")
                self.window.quit()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.window.quit()
            self.player_turn = "O" if self.player_turn == "X" else "X"

    def check_win(self):
        for row in self.buttons:
            if row[0]['text'] == row[1]['text'] == row[2]['text'] != "":
                return True
        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text'] != "":
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True
        return False

    def check_draw(self):
        for row in self.buttons:
            for button in row:
                if button['text'] == "":
                    return False
        return True
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()