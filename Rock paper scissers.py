import random

moves = ["rock", "paper", "scissors"]


class Player:

    score = 0
    my_move = ""
    their_move = ""

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):

    def move(self):
        choose = input("Rock, Paper, Scissors? > ").lower()
        if choose in moves:
            return choose
        else:
            self.move()


class ReflectPlayer(Player):

    def move(self):
        if self.their_move in moves:
            return self.their_move
        else:
            return random.choice(moves)


class CyclePlayer(Player):

    def move(self):
        if self.my_move == "rock":
            return "paper"
        if self.my_move == "paper":
            return "scissors"
        elif self.my_move == "scissors":
            return "rock"
        else:
            return random.choice(moves)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.name = "You"
        self.p2.name = "computer"

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"{self.p1.name} played {move1}.")
        print(f"{self.p2.name} played {move2}.\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if move1 == move2:
            print("** TIE **\n")
            print(f"Score: {self.p1.name} {self.p1.score}, "
                  f"{self.p2.name} {self.p2.score}")
        elif beats(move1, move2):
            print(f"** PLAYER ONE WINS **\n")
            self.p1.score += 1
            print(f"Score: {self.p1.name} {self.p1.score}, "
                  f"{self.p2.name} {self.p2.score}")
        else:
            print(f"** PLAYER Two WINS **\n")
            self.p2.score += 1
            print(f"Score: {self.p1.name} {self.p1.score}, "
                  f"{self.p2.name} {self.p2.score}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        print("===========================================")
        print(f"Player one: {self.p1.name}   VS   Player two: {self.p2.name}")
        print("===========================================")
        print("Rock paper scissors, Go!\n")
        for round in range(6):
            print(f"Round {round} --")
            self.play_round()
        print("GAME OVER")
        if self.p1.score > self.p2.score:
            print(f"{self.p1.name} is the WINNER")
        elif self.p1.score < self.p2.score:
            print(f"{self.p2.name} is the WINNER")
        else:
            print("TIE ~ No winner!\n")
        ask = input("Would you like to play again? yes/no  ").lower()
        if ask == "yes":
            self.play_game()
        else:
            exit(0)


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
