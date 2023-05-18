#pip install easyAI
from easyAI import TwoPlayerGame, AI_Player, Human_Player, Negamax

class TicTacToe(TwoPlayerGame):
    def __init__(self, players):
        self.players = players
        self.board = [0] * 9
        self.current_player = 1

    def possible_moves(self):
        return [i + 1 for i, e in enumerate(self.board) if e == 0]

    def make_move(self, move):
        self.board[move - 1] = self.current_player

    def unmake_move(self, move):
        self.board[move - 1] = 0

    def lose(self):
        lines = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        return any(all(self.board[c - 1] == self.opponent_index for c in line) for line in lines)

    def is_over(self):
        return not self.possible_moves() or self.lose()

    def show(self):
        print("\n".join(" ".join([".", "O", "X"][self.board[3 * j + i]] for i in range(3)) for j in range(3)))

    def scoring(self):
        return -100 if self.lose() else 0


if __name__ == "__main__":
    ai_algo = Negamax(6)
    TicTacToe([Human_Player(), AI_Player(ai_algo)]).play()
