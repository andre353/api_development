class Alphabet:
    def __init__(self, title, abbreviation, letters):
        self.title = title
        self.abbreviation = abbreviation
        self.letters = letters
        print("A new alphabet has been created!")

    def describe(self):
        description = f"The {self.title} alphabet contains the following letters: {self.letters}. It is abbreviated as {self.abbreviation}."
        return description

    def count_letters(self):
        return len(self.letters) 


class Cyrillic(Alphabet):
    def __init__(self, title, abbreviation, letters):
        super().__init__(title, abbreviation, letters)
        self.language_group = "Slavic"

    def describe(self):
        description = f"The {self.title} alphabet contains the following letters: {self.letters}. It is abbreviated as {self.abbreviation}. It belongs to the {self.language_group} language group."
        return description

serbian = Cyrillic("Serbian", "SR", "абвгдђежзијклмнњопрстћуфхцчџшыэ")           
print(serbian.describe())     

