import random
from typing import Iterable

from game_status import GameStatus
from invalid_operation_error import InvalidOperationError


class Game:
    def __init__(self, mistakes: int = 6):
        if mistakes < 5 or mistakes > 8:
            raise ValueError("Число попыток должно быть не меньше 5 и не больше 8!")
        self.__mistakes = mistakes  # количество попыток
        self.__counter = 0  # счётчик попыток
        self.__word = ""
        self.__used_letters = []  # использованные буквы
        self.__open_letters = ""  # открытые буквы
        self.__progress = []  # Открытые буквы в слове
        self.__game_status = GameStatus.NOT_STARTED

    def generate_word(self) -> str:
        self.__word = random.choice(open("WordsStockRus.txt").read().split())
        self.__progress = ["-"] * len(self.__word)
        self.__game_status = GameStatus.IN_PROGRESS
        return self.__word

    def letter_transmission(self, letter: str) -> Iterable[str]:
        if self.__counter == self.__mistakes:
            raise InvalidOperationError(
                f"Использовано максимальное количество попыток. Всего допустимо {self.__mistakes}")

        if self.__game_status != GameStatus.IN_PROGRESS:
            raise InvalidOperationError(f"Текущий статус игры: {self.__game_status}")

        self.__used_letters.append(letter)

        if letter in self.__word:
            self.__open_letters += letter
            for i in range(len(self.__word)):
                if self.__progress[i] == '-' and self.__word[i] == letter:
                    self.__progress[i] = letter
        else:
            self.__counter += 1

        if self.__is_winning():
            self.__game_status = GameStatus.WON
        elif self.__counter == self.__mistakes:
            self.__game_status = GameStatus.LOST

        return self.__progress

    def __is_winning(self):
        if set(self.__open_letters) == set(self.__word):
            return True
        else:
            return False

    @property
    def progress(self):
        return self.__progress

    @property
    def mistakes(self):
        return self.__mistakes

    @property
    def counter(self):
        return self.__counter

    @property
    def word(self):
        return self.__word

    @property
    def used_letters(self) -> Iterable[str]:
        return sorted(self.__used_letters)

    @property
    def game_status(self):
        return self.__game_status

    @property
    def remaining_tries(self):
        return self.__mistakes - self.__counter
