class StringReverse:
    def __init__(self, text=""):
        self.__text = text

    def set_text(self, text):
        self.__text = text

    def get_text(self):
        return self.__text

    def reverse_words(self) -> str:
        words = self.__text.split()
        return " ".join(words[::-1])

