class Drawer:
    def draw(self, mistakes):
        with open("assets/hangman%d.txt" % mistakes, "r") as file:
            file_content = file.read()
            print(file_content)
