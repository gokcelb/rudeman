class Word:
    def __init__(self, word, difficulty, category):
        self.word = word
        self.difficulty = difficulty
        self.category = category


words = [
    Word("COMPUTER", "easy", "technology"),
    Word("DRIVER", "medium", "technology"),
    Word("MOUSE", "easy", "technology"),
    Word("KEYBOARD", "medium", "technology"),
    Word("MOTHER BOARD", "hard", "technology"),
    Word("CENTRAL PROCESSING UNIT", "hard", "technology"),
    Word("MONITOR", "medium", "technology"),
    Word("MEGABYTE", "hard", "technology"),
    Word("CAR", "easy", "vehicle"),
    Word("BUS", "easy", "vehicle"),
    Word("TRUCK", "medium", "vehicle"),
    Word("BULDOZER", "hard", "vehicle"),
    Word("BICYCLE", "medium", "vehicle"),
    Word("DUMP TRUCK", "hard", "vehicle"),
    Word("TAXI", "medium", "vehicle"),
    Word("GLIDER", "hard", "vehicle"),
]
