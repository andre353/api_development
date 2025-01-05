from baseClass import Alphabet, Cyrillic

russian = Alphabet("Russian", "RU", "абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
russian.describe()
russian.count_letters()

serbian = Cyrillic("Serbian", "SR", "абвгдђежзијклмнњопрстћуфхцчџшыэ")
serbian.describe()
serbian.count_letters()
