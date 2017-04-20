# coding=utf-8

q_and_a = {
    'easy': {
        'question': '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,tuple, and ___4___ or can be more complicated such as objects and lambda functions. ''',
        'answer': [
            {'question_id': '1', 'list_answer': ["function", "Function"], 'first_letter': 'F'},
            {'question_id': '2', 'list_answer': ["argument", "Argument"], 'first_letter': 'A'},
            {'question_id': '3', 'list_answer': ["none", "None"], 'first_letter': 'N'},
            {'question_id': '4', 'list_answer': ["list", "List"], 'first_letter': 'L'}
        ]
    },
    'medium': {
        'question': '''A ___1___ program is usually written by a ___1___ programmer in a programming language. From the program in its human-readable form of source code, a ___2___ can derive machine code : a form consisting of ___3___ that the ___1___ can directly execute. Alternatively, a ___1___ program may be executed with the aid of an ___4___. ''',
        'answer': [
            {'question_id': '1', 'list_answer': ["computer", "Computer"], 'first_letter': 'C'},
            {'question_id': '2', 'list_answer': ["compiler", "Compiler"], 'first_letter': 'C'},
            {'question_id': '3', 'list_answer': ["instructions", "Instructions"], 'first_letter': 'I'},
            {'question_id': '4', 'list_answer': ["interpreter", "Interpreter"], 'first_letter': 'I'}
        ]
    },
    'hard': {
        'question': '''___1___ are small, chubby, and incredibly cute mouse-like Pokémon. They are almost completely covered by ___2___ fur. They have long ___2___ ears that are tipped with black. A ___1___'s back has two brown stripes, and its large tail is notable for being shaped like a lightning bolt. On its ___3___ are two circle-shaped red pouches used for storing ___4___. They turn ___2___ and spark with ___4___ when its about to use an Electric attack, such as Thunderbolt. It has also been known to ___5___ small surges of electrical energy in anger or for protection, like in the anime. ''',
        'answer': [
            {'question_id': '1', 'list_answer': ["pikachu", "Pikachu"], 'first_letter': 'P'},
            {'question_id': '2', 'list_answer': ["yellow", "Yellow"], 'first_letter': 'Y'},
            {'question_id': '3', 'list_answer': ["cheeks", "Cheeks"], 'first_letter': 'C'},
            {'question_id': '4', 'list_answer': ["electricity", "Electricity"], 'first_letter': 'E'},
            {'question_id': '5', 'list_answer': ["generate", "Generate"], 'first_letter': 'G'}
        ]

    }
}


def check_answer(question, q_id, list_ans, first_letter):
    """Checks the answer is correct or not. Returns True if correct."""
    answer = raw_input("Which statement should it put in ___" + q_id + "___? ")
    if answer == list_ans[0] or answer == list_ans[1]:
        print "answer is correct. ___" + q_id + "___ is " + list_ans[0] + "."
        index = 0

        for whatever in question:
            question[index] = question[index].replace("___" + q_id + "___", list_ans[0])
            index += 1

        print " ".join(question)
        print ""
        return True
    else:
        print "That's not the correct answer. Hint: It starts with " + first_letter + "."
        return False


def game(level):
    """ level :  easy, medium, hard"""

    print "Your difficulty level is " + level
    question = q_and_a[level]['question']
    list_answer = q_and_a[level]['answer']

    print question
    question = question.split(" ")

    for answer in range(len(list_answer)):
        while not check_answer(question, list_answer[answer]['question_id'], list_answer[answer]['list_answer'], list_answer[answer]['first_letter']):
            print ""

    print "Final answer:"
    print " ".join(question)
    return


def main():
    """Function for the main game"""
    game(raw_input("select difficulty level, easy,medium,or hard: "))

main()
