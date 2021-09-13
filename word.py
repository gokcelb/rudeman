class Word:
    def __init__(self, word, difficulty, category):
        self.word = word
        self.difficulty = difficulty
        self.category = category


    def get_score(self):
        if self.difficulty == "easy":
            score = 5
        elif self.difficulty == "medium":
            score = 10
        elif self.difficulty == "hard":
            score = 20
        return score

    def __str__(self) -> str:
        return "word: {}, difficulty: {}, category: {}".format(
            self.word, self.difficulty, self.category)
        

words = [
    Word("COMPUTER", "easy", "technology"),
    Word("DRIVER", "medium", "technology"),
    Word("MOUSE", "easy", "technology"),
    Word("KEYBOARD", "medium", "technology"),
    Word("MOTHER BOARD", "hard", "technology"),
    Word("CENTRAL PROCESSING UNIT", "hard", "technology"),
    Word("CAR", "easy", "vehicle"),
    Word("BUS", "easy", "vehicle"),
    Word("TRUCK", "medium", "vehicle"),
    Word("BULDOZER", "hard", "vehicle"),
    Word("BICYCLE", "medium", "vehicle"),
    Word("DUMP TRUCK", "hard", "vehicle"),
    Word("TAXI", "medium", "vehicle"),
    Word("GLIDER", "hard", "vehicle"),
    ]