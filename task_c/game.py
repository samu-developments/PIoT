import csv, time, sys

from sense_hat import SenseHat

from electronic_die import SenseDie


class DieGame:
    def __init__(self, sense: SenseHat, goal: int):
        self.sense = sense
        self.goal = goal
        self.die = SenseDie(sense)
        self.player_a_score = 0
        self.player_b_score = 0
        self.round = 1  # this makes player A start

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
            self.player_b_score += self.die.detect_roll()
        else:
            self.sense.show_letter("A")
            self.player_a_score += self.die.detect_roll()
        self.round += 1

    def is_finished(self):
        return self.player_a_score > self.goal or self.player_b_score > self.goal

    def finish_game(self):
        winner = 'A' if self.player_a_score > self.player_b_score else 'B'
        score = max(self.player_a_score, self.player_b_score)
        self.sense.show_message(f"Player {winner} wins!")
        with open('winner.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([f"Winner: {winner}", f"Score: {score}", f"Time: {time.ctime()}"])


if __name__ == '__main__':
    goal = sys.argv[1] if len(sys.argv) > 1 else 10
    sense = SenseHat()
    game = DieGame(sense, goal)
    game.start_game()
