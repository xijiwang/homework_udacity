# coding=utf-8

q_and_a = {
    'easy': {
        'question': '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,tuple, and ___4___ or can be more complicated such as objects and lambda functions. ''',
        'answer': [
            ['1', ["function", "Function"], 'F'],
            ['2', ["argument", "Argument"], 'A'],
            ['3', ["none", "None"], 'N'],
            ['4', ["list", "List"], 'L']
        ]
    },
    'medium': {
        'question': '''A ___1___ program is usually written by a ___1___ programmer in a programming language. From the program in its human-readable form of source code, a ___2___ can derive machine code : a form consisting of ___3___ that the ___1___ can directly execute. Alternatively, a ___1___ program may be executed with the aid of an ___4___. ''',
        'answer': [
            ['1', ["computer", "Computer"], 'C'],
            ['2', ["compiler", "Compiler"], 'C'],
            ['3', ["instructions", "Instructions"], 'I'],
            ['4', ["interpreter", "Interpreter"], 'I']]
    },
    'hard': {
        'question': '''___1___ are small, chubby, and incredibly cute mouse-like Pokémon. They are almost completely covered by ___2___ fur. They have long ___2___ ears that are tipped with black. A ___1___'s back has two brown stripes, and its large tail is notable for being shaped like a lightning bolt. On its ___3___ are two circle-shaped red pouches used for storing ___4___. They turn ___2___ and spark with ___4___ when its about to use an Electric attack, such as Thunderbolt. It has also been known to ___5___ small surges of electrical energy in anger or for protection, like in the anime. ''',
        'answer': [
            ['1', ["pikachu", "Pikachu"], 'P'],
            ['2', ["yellow", "Yellow"], 'Y'],
            ['3', ["cheeks", "Cheeks"], 'C'],
            ['4', ["electricity", "Electricity"], 'E'],
            ['5', ["generate", "Generate"], 'G']
        ]
    }
}


def check_answer(question, q_id, list_ans, first_letter):
    """Checks the answer is correct or not. Returns True if correct."""
    answer = raw_input("Which statement should it put in ___" + q_id + "___? ")
    if answer == list_ans[0] or answer == list_ans[1]:
        print "answer is correct. ___" + q_id + "___ is " + list_ans[0] + "."
        idx = 0

        for whatever in question:
            question[idx] = question[idx].replace("___" + q_id + "___", list_ans[0])
            idx += 1

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

    for i in range(len(list_answer)):
        while not check_answer(question, list_answer[i][0], list_answer[i][1], list_answer[i][2]):
            print ""

    print "Final answer:"
    print " ".join(question)
    return


def main():
    """Function for the main game"""
    game(raw_input("select difficulty level, easy,medium,or hard: "))

main()
