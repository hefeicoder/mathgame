import random

def question_multiplication_single_digit():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)

    operation = "*"
    question = f"{num1} {operation} {num2}"
    correct_answer = eval(question)

    return question, correct_answer


def question_addition_within_twenty():
    while True:
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operation = random.choice(["+", "-"])
        question = f"{num1} {operation} {num2}"
        correct_answer = eval(question)

        if 0 <= correct_answer <= 20:
            return question, correct_answer