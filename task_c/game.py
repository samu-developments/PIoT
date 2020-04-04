import csv, time, sys
from typing import List

from sense_hat import SenseHat

from electronic_die import SenseDie


class Player:
    def __init__(self, id: str):
        self.id = id
        self.score = 0

    def __str__(self):
        return self.id


class DieGame:
    def __init__(self, sense: SenseHat, goal: int, players: List[Player]):
        self.sense = sense
        self.goal = goal
        self.die = SenseDie(sense)
        self.players = players

    def show_instructions(self):
        self.sense.show_message(f"Shake die, first to {self.goal}. Player {self.players[0]} begin!")

    def start_game(self):
        self.show_instructions()
        winner = None
        while winner is None:
            for player in self.players:
                self.play(player)
                time.sleep(1)
            winner = DieGame.is_finished(self.players, self.goal)
        return self.finish_game(winner)

    def play(self, player: Player) -> int:
        self.sense.show_letter(player.id)
        player.score += self.die.detect_roll()
        return player.score

    # Returns winner or None
    @staticmethod
    def is_finished(players: List[Player], goal: int) -> Player:
        leader = players[0]
        for p in players:
            if p.score > leader.score:
                leader = p
        return leader if leader.score >= goal else None

    def finish_game(self, winner: Player):
        self.sense.show_message(f"Player {winner} wins!")
        with open('winner.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([f"Winner: {winner}", f"Score: {winner.score}", f"Time: {time.ctime()}"])


if __name__ == '__main__':
    sense = SenseHat()
    goal = sys.argv[1] if len(sys.argv) > 1 else 10
    try:
        goal = int(goal)
    except ValueError:
        sense.show_message(f"Arg <{goal}> must be int, exiting.")
        sys.exit()
    player1, player2 = Player('A'), Player('B')
    game = DieGame(sense, goal, [player1, player2])
    game.start_game()
