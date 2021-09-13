import word
import random
from draw import Drawer


class Hangman:
    def __init__(self, words) -> None:
        self.words = words
        self.drawer = Drawer()


    def categorize_words(self) -> list:
        category = input("Which category do you choose? Technology or vehicle?").lower()
        print()

        categorized_words = []
        for word in self.words:
            if word.category == category:
                categorized_words.append(word.word)

        return categorized_words

    
    def random_word_from_categorized_words(self) -> str:
        categorized_words = self.categorize_words()

        random_index = random.randint(0, len(categorized_words)-1)
        random_word = categorized_words[random_index]

        return random_word


    def get_letter(self) -> str:
        return input("Type in a letter: ").upper()


    def letter_exists(self, letter, word) -> bool:
        if letter in word:
            return True
        return False


    def print_underscores(self, underscores):
        for underscore in underscores:
            print(underscore, end="")
        print()    


    def place_letter(self, letter, word, underscores):
        indexes = []
        for i in range(len(word)):
            if word[i] == letter:
                indexes.append(i)

        for i in indexes:
            underscores[i] = letter

        self.print_underscores(underscores)


    def start_game(self):
        random_word = self.random_word_from_categorized_words()

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
                print("You already found this letter.")

            if self.letter_exists(letter, random_word):
                self.place_letter(letter, random_word, underscores)
            else:
                remaining_wrong_guesses -= 1
                mistakes += 1
                print("{} not in word.".format(letter))
                self.drawer.draw(mistakes)
                self.print_underscores(underscores)

        if remaining_wrong_guesses == 0:
            print("Congragulations! You hanged the man you worthless piece of garbage.")


if __name__ == "__main__":
    game = Hangman(word.words)
    game.start_game()