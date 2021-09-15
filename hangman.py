import word
import random
from draw import Drawer


class Hangman:
    def __init__(self, words) -> None:
        self.words = words
        self.drawer = Drawer()

    def categorize_words(self) -> list:
        category = input(
            "Which category do you choose? Technology or vehicle?").lower()
        print()
        while category != "vehicle" and category != "technology":
            category = input('Wrong input. Type in "technology" or "vehicle".')
            print()

        categorized_words = []
        for word in self.words:
            if word.category == category:
                categorized_words.append(word.word)

        random.shuffle(categorized_words)
        return categorized_words

    def get_score(self, random_word):
        for word in self.words:
            if word.word == random_word:
                if word.difficulty == "easy":
                    score = 5
                elif word.difficulty == "medium":
                    score = 10
                elif word.difficulty == "hard":
                    score = 20
                return score

    def get_letter(self) -> str:
        return input("Type in a letter: ").upper()

    def letter_exists(self, letter, word) -> bool:
        return letter in word

    def print_underscores(self, underscores):
        for underscore in underscores:
            print(underscore, end="")
        print()

    def place_letter(self, letter, word, underscores):
        for i in range(len(word)):
            if word[i] == letter:
                underscores[i] = letter

        self.print_underscores(underscores)

    def start_game(self):
        categorized_words = self.categorize_words()
        n = len(categorized_words)
        score = 0

        while n > 0:
            random_word = categorized_words[n-1]
            underscores = ["_"] * len(random_word)
            for i in range(len(random_word)):
                if random_word[i] == " ":
                    underscores[i] = " "
            self.print_underscores(underscores)

            remaining_wrong_guesses = 10
            mistakes = 0

            while "_" in underscores and remaining_wrong_guesses > 0:
                print()
                letter = self.get_letter()
                if letter in underscores:
                    print("\nYou already found this letter.")
                    self.print_underscores(underscores)
                elif self.letter_exists(letter, random_word):
                    self.place_letter(letter, random_word, underscores)
                else:
                    remaining_wrong_guesses -= 1
                    mistakes += 1
                    print("\n{} not in word.".format(letter))
                    self.drawer.draw(mistakes)
                    self.print_underscores(underscores)

            if remaining_wrong_guesses == 0:
                print(
                    "\nCongragulations! You hanged the man you worthless piece of garbage.")
                break
            else:
                score += self.get_score(random_word)
            print("\nYour current score: %d\n\nNEW WORD" % score)
            n -= 1

        if score == 100:
            print("\nYou absolutely killed it! What a total surprise!")


if __name__ == "__main__":
    game = Hangman(word.words)
    game.start_game()
