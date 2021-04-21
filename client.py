from Viselitsa import Game
from game_status import GameStatus


def chars_list_to_str(ch):
    return ''.join(ch)


game = Game(10)
word = game.generate_word()

letter_count = len(word)

print(f"Слово состоит из {letter_count} букв.")
print("Попробуй угадать слово по буквам.")

while game.game_status == GameStatus.IN_PROGRESS:
    letter = input("Введите букву\n")
    state = game.letter_transmission(letter)
    print(chars_list_to_str(state))
    print(f"Использованны буквы: {chars_list_to_str(game.used_letters)}")
    print(f"Осталось попыток: {game.remaining_tries}")

if game.game_status == GameStatus.LOST:
    print("Вы проиграли...")
    print(f"Было загадано слово - {game.word}")
else:
    print("Вы победили!")
