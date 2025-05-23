"""Создание опросника"""


import random


def quiz(data: dict, question):
    questions_list = list(data.keys())
    random.shuffle(questions_list)
    right_answers = 0
    wrong_answers = 0
    for q in questions_list:
        right_answer = data[q]
        all_answers = list(data.values())
        del all_answers[all_answers.index(right_answer)]
        variants = random.sample(all_answers, 3)
        variants.append(right_answer)
        random.shuffle(variants)
        print("-" * 40)
        print(f"{question}{q.upper()}")
        for i, var in enumerate(variants):
            print(f"\t{i+1}. {var}")
        print()
        while True:
            answer = input("Введите номер ответа: ")
            if not answer.isnumeric():
                print("Вы ввели НЕ число")
            elif int(answer) not in (range(1, len(variants) + 1)):
                print("Нет такого варианта ответа")
            else:
                answer = int(answer)
                break
        if variants[int(answer) - 1] == right_answer:
            right_answers += 1
        else:
            wrong_answers += 1
    print("Результат опроса:")
    print(f"\tВы верно ответили {right_answers} раз(а)")
    print(f"\tВы ошиблись {wrong_answers} раз(а)")


if __name__ == "__main__":

    print("опрос на знание названий цветов".upper().center(120))
    english_colors = {
        "white": "белый",
        "black": "черный",
        "red": "красный",
        "green": "зеленый",
        "blue": "синий",
        "yellow": 'желтый',
        "gray": "серый",
        "brown": "коричневый",
        "violet": "фиолетовый",
        "orange": "оранжевый",
        "maroon": "бордовый",
    }

    english_animals = {
        "cat": "кошка",
        "dog": "собака",
        "rat": "крыса",
        "bat": "летучая мышь",
        "monkey": "обезьяна",
        "crocodile": 'крокодил',
        "elephant": "слон",
        "mouse": "мышь",
        "snake": "змея",
        "horse": "лошадь",
        "pig": "свинья",
        "frog": "лягушка",
        "bird": "птица",
        "squirrel": "белка",
        "wolf": "волк",
        "fox": "лиса",
        "bear": "медведь",
        "deer": "олень",
        "elk": "лось",
        "lion": "лев",
        "tiger": "тигр",
        "Rhinoceros": 'носорог',
        "giraffe": 'жираф',
        "cow": 'корова',
        "sheep": "овца",
        "chicken": "курица",
        "rooster": "петух",
    }

    # quiz(english_colors, "Как переводится слово: ")
    quiz(english_animals, "Как переводится слово: ")
