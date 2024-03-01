import streamlit as st
import random as rand

players = ["X", "O"]

board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

turn = rand.choice(players)

def nextGame():
    global turn, board
    turn = rand.choice(players)
    st.session_state.board = [["", "", ""],
                              ["", "", ""],
                              ["", "", ""]]
    st.session_state.turn = turn
    st.session_state.game_status = f"{turn}'s turn"

def isEmptySpaces():
    totalSpace = 9
    for row in range(3):
        for col in range(3):
            if st.session_state.board[row][col] != "":
                totalSpace -= 1
    return totalSpace > 0

def checkWinner():
    for i in range(3):
        if st.session_state.board[i][0] == st.session_state.board[i][1] == st.session_state.board[i][2] and st.session_state.board[i][0] != "":
            return True
        if st.session_state.board[0][i] == st.session_state.board[1][i] == st.session_state.board[2][i] and st.session_state.board[0][i] != "":
            return True
    if st.session_state.board[0][0] == st.session_state.board[1][1] == st.session_state.board[2][2] and st.session_state.board[0][0] != "":
        return True
    if st.session_state.board[0][2] == st.session_state.board[1][1] == st.session_state.board[2][0] and st.session_state.board[0][2] != "":
        return True
    return False

def nextTurn(row, column):
    if st.session_state.board[row][column] == "" and not checkWinner():
        st.session_state.board[row][column] = st.session_state.turn
        if not checkWinner():
            st.session_state.turn = players[(players.index(st.session_state.turn) + 1) % 2]
            st.session_state.game_status = f"{st.session_state.turn}'s turn"
        elif checkWinner():
            st.session_state.game_status = f"{st.session_state.turn} won"
        elif not isEmptySpaces():
            st.session_state.game_status = "Tie"

if "board" not in st.session_state:
    nextGame()

st.title("Tic-Tac-Toe")

st.write("Tic-Tac-Toe")

st.button("Next Game", on_click=nextGame)

st.write(st.session_state.game_status)

board_container = st.container()

with board_container:
    for i in range(3):
        row_container = st.container()
        for j in range(3):
            cell = st.session_state.board[i][j]
            if cell == "":
                clicked = row_container.button("", key=f"{i}_{j}", on_click=nextTurn, args=(i, j))
            else:
                row_container.write(cell)
