import streamlit as st
import random as rand

players = ["X", "O"]

def initialize_game():
    return [["" for _ in range(3)] for _ in range(3)], rand.choice(players)

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True

    return False

def next_game():
    st.session_state.board, st.session_state.current_player = initialize_game()

def make_move(row, col):
    board = st.session_state.board
    if board[row][col] == "" and not check_winner(board):
        board[row][col] = st.session_state.current_player
        st.session_state.current_player = players[(players.index(st.session_state.current_player) + 1) % 2]

def main():
    if "board" not in st.session_state:
        next_game()

    st.title("Tic-Tac-Toe")
    st.button("Next Game", on_click=next_game)

    for i in range(3):
        row = st.empty()
        for j in range(3):
            cell = st.session_state.board[i][j]
            if cell == "":
                clicked = row.button("", key=f"{i}_{j}", on_click=make_move, args=(i, j))
            else:
                row.write(cell)

if __name__ == "__main__":
    main()
