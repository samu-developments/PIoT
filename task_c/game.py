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
        #self.show_instructions()
        winner = None
        while winner is None:
            for player in self.players:
                self.play(player)
                time.sleep(1)
            winner = DieGame.is_finished(self.players, self.goal)
        return self.finish_game(winner)

    def play(self, player: Player) -> int:
        if len(player.id) > 1:
            self.sense.show_message(player.id)
        else:
            self.sense.show_letter(player.id)
        player.score += self.die.detect_roll()
        return player.score

    # Returns winner or None
    @staticmethod
    def is_finished(players: List[Player], goal: int) -> List[Player]:
        leader = [players[0]]
        for p in players:
            if p.score > leader[0].score:
                leader = [p]
            elif p.score == leader[0].score and p.id is not leader[0].id:
                leader.append(p)
        return leader if leader[0].score >= goal else None

    def finish_game(self, winners: List[Player]):
        winner_str = ','.join([w.id for w in winners])
        if len(winners) >= 2:
            self.sense.show_message(f"Tie! {winner_str} wins!")
        else:
            self.sense.show_message(f"Player {winner_str} wins!")
        with open('winner.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            t = time.ctime()
            for w in winners:
                writer.writerow([f"Winner: {w.id}", f"Score: {w.score}", f"Time: {t}"])


if __name__ == '__main__':
    sense = SenseHat()
    goal = sys.argv[1] if len(sys.argv) > 1 else 10
    players = []
    if len(sys.argv) >= 3:
        players = [Player(id) for id in sys.argv[2:]]
    else:
        players = [Player('A'), Player('B')]
    try:
        goal = int(goal)
    except ValueError:
        sense.show_message(f"First arg <{goal}> must be int, exiting.")
        sys.exit()
    game = DieGame(sense, goal, players)
    game.start_game()
