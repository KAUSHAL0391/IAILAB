from typing import List, Tuple

# Class to represent a state in the 8-puzzle problem.
class State:
    def __init__(self, board: List[List[int]]):
        self.board = board

    # Function to check if the state is the goal state.
    def is_goal(self) -> bool:
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return self.board == goal_state

    # Function to get the neighbors of the state.
    def get_neighbors(self) -> List['State']:
        neighbors = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    # Move the blank tile up.
                    if i > 0:
                        new_board = [row[:] for row in self.board]
                        new_board[i][j], new_board[i-1][j] = new_board[i-1][j], new_board[i][j]
                        neighbors.append(State(new_board))
                    # Move the blank tile down.
                    if i < 2:
                        new_board = [row[:] for row in self.board]
                        new_board[i][j], new_board[i+1][j] = new_board[i+1][j], new_board[i][j]
                        neighbors.append(State(new_board))
                    # Move the blank tile left.
                    if j > 0:
                        new_board = [row[:] for row in self.board]
                        new_board[i][j], new_board[i][j-1] = new_board[i][j-1], new_board[i][j]
                        neighbors.append(State(new_board))
                    # Move the blank tile right.
                    if j < 2:
                        new_board = [row[:] for row in self.board]
                        new_board[i][j], new_board[i][j+1] = new_board[i][j+1], new_board[i][j]
                        neighbors