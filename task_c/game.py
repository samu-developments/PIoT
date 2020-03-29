import csv, time

from sense_hat import SenseHat

from electronic_die import SenseDie


class DieGame:
    def __init__(self, sense: SenseHat, goal: int):
        self.sense = sense
        self.goal = goal
        self.die = SenseDie(sense)
        self.player_a_score = 0
        self.player_b_score = 0
        self.round = 0

    def show_instructions(self):
        self.sense.show_message("Shake die, first to 30. Player 1 begin!")

    def play(self, round: int):
        while not self.is_finished():
            if round % 2 == 0:
                self.sense.show_message("B:")
                self.player_b_score += self.die.detect_roll()

            else:
                self.sense.show_message("A:")
                self.player_a_score += self.die.detect_roll()
            round += 1
            time.sleep(1)
        self.finish_game()

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
    goal = 10
    sense = SenseHat()
    game = DieGame(sense, 10)
    game.play(0)
