import os
import time


class BingoBoard:
    def __init__(self, entries) -> None:
        self.entries = entries
        self.entries_dict = {}
        for i, e in enumerate(self.entries):
            self.entries_dict[e] = i
        self.found = [False] * 25
        self.won = False
        self.winning_number = -1
        self.result = 0
        self.winning_round = 0

    def reset(self):
        self.found = [False] * 25
        self.won = False
        self.winning_number = -1
        self.result = 0
        self.winning_round = 0

    def playNumber(self, number):
        if self.won:
            return
        self.winning_round += 1
        if number in self.entries_dict:
            self.found[self.entries_dict[number]] = True
            self.checkWin()
            if self.won:
                self.winning_number = number
                self.calcResult()

    def checkWin(self):

        if self.won:
            return
        else:
            # check rows
            for i in range(5):
                if all(self.found[j] for j in range(5*i, 5*i+5)):
                    self.won = True
            # check cols
            for i in range(5):
                if all(self.found[j] for j in range(i, 25+i, 5)):
                    self.won = True

    def calcResult(self):
        self.result = sum(self.entries[i] if not self.found[i] else 0 for i in range(
            25))*self.winning_number

    def __repr__(self) -> str:
        rep = ""
        for i in range(25):
            if self.found[i]:
                rep += "*\t"
            else:
                rep += str(self.entries[i])+"\t"
            if i % 5 == 4:
                rep += "\n"
        return rep


def main():
    # input
    print(os.getcwd())
    day = "04"
    year = "2021"
    inputFile = f'../inputs/day{day}.txt'
    print(inputFile)
    part1, part2 = 0, 0
    with open(inputFile) as f:
        lines = f.read().splitlines()
    numbers = list(map(int, lines[0].split(",")))
    boards = []
    # read bingo boards
    for i in range(1, len(lines), 6):
        entries = []
        for j in range(i+1, i+6):
            entries.extend(list(map(int, lines[j].split())))
        boards.append(BingoBoard(entries))
    start_time = time.time()

    game_finished = False
    for n in numbers:
        if game_finished:
            break
        for b in boards:
            b.playNumber(n)
            if b.won:
                part1 = b.result
                game_finished = True
                break

    # part2
    for b in boards:
        b.reset()
    for n in numbers:
        for b in boards:
            b.playNumber(n)
        if all(b.won for b in boards):
            break

    p2a = [(b.result, b.winning_round) for b in boards]
    p2as = sorted(p2a, key=lambda tup: tup[1], reverse=True)

    part2 = p2as[0][0]

    duration = int((time.time() - start_time) * 1000000)

    print(
        f"AoC {year} - Day {day}:\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nDuration:\t{duration} ns")


if __name__ == "__main__":
    main()
