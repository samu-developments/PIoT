import csv, time, sys

from sense_hat import SenseHat

from electronic_die import SenseDie


class Player:
    def __init__(self, id: str):
        self.id = id
        self.score = 0

    def __str__(self):
        return self.id


class DieGame:
    def __init__(self, sense: SenseHat, goal: int, player1: Player, player2: Player):
        self.sense = sense
        self.goal = goal
        self.die = SenseDie(sense)
        self.player1 = player1
        self.player2 = player2
        self.round = 1  # this makes player 1 start

    def show_instructions(self):
        self.sense.show_message("Shake die, first to 30. Player A begin!")

    def start_game(self):
        # self.show_instructions()
        while not self.is_finished():
            self.play()
            time.sleep(1)
        self.finish_game()

    def play(self):
        if self.round % 2 == 0:
            self.sense.show_letter("B")
            self.player2.score += self.die.detect_roll()
        else:
            self.sense.show_letter("A")
            self.player1.score += self.die.detect_roll()
        self.round += 1

    def is_finished(self):
        return self.player1.score > self.goal or self.player2.score > self.goal

    def finish_game(self):
        winner = self.player1 if self.player1.score > self.player2.score else self.player2
        score = winner.score
        self.sense.show_message(f"Player {winner} wins!")
        with open('winner.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([f"Winner: {winner}", f"Score: {winner.score}", f"Time: {time.ctime()}"])


if __name__ == '__main__':
    goal = sys.argv[1] if len(sys.argv) > 1 else 10
    sense = SenseHat()
    player1, player2 = Player('A'), Player('B')
    game = DieGame(sense, goal, player1, player2)
    game.start_game()
