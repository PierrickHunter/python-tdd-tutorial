class Set:
    def __init__(self):
        self.first = 0
        self.second = 0
        self.scores = Scores()
    def firstScores(self):
        self.first = self.first + 1
    def firstScore(self):
        return self.scores.scoreName(self.first)
    def secondScores(self):
        self.second = self.second + 1
    def secondScore(self):
        return self.scores.scoreName(self.second)

class Scores:
    def __init__(self):
        self.scoreNames = ["0", "15", "30", "40", "A"]
    def scoreName(self, index):
        return self.scoreNames[index]
