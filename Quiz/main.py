import os
from questions import quest


def ask_question():

    answer = []

    for key, value in quest.items():
        answers = input(f"{key}. {value}")
        answer.append(f'{key}. {answers}')
        if answers == '':
            print("Error! you must provide an answer to this question")
            break
        else:
            with open('answers.txt', 'w') as ans:
                for values in answer:
                    ans.write(f'{values} \n')


ask_question()
