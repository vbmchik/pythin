class Doc():

    def __init__(self, filename) -> None:
        self.filename = filename
        self.secure=True

    def readFile(self):
        with open(self.filename) as file:
            self.text = file.read()
    


text = Doc('advs.txt')
text.readFile()

print(
    text.text, text.secure
)
