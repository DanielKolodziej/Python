from question import Question

questionList = [
    "What is the color of an orange? (a)red(b)blue(c)orange",
    "What is the letter after a? (a)a(b)b(c)c"
]

questions = [
    Question(questionList[0], 'c'),
    Question(questionList[1], 'b')
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    # print(f'You got {score}/{len(questions)} correct')
    print('You got ' + str(score) + '/' + str(len(questions)) + ' correct')


run_test(questions)
