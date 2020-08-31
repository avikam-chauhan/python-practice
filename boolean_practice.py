import random

difficulty_level = 1
tests_per_level = 5

operators = [" and ", " or "]
prefix = ["not ", ""]
values = ["True", "False", "random.randint(0, 10)", "None"]

def generate_random_boolean_operator():
    return operators[random.randint(0, len(operators) - 1)]

def generate_random_value():
    return prefix[random.randint(0, len(prefix) - 1)] + str(eval(values[random.randint(0, len(values) - 1)]))

def generate_boolean_statement(n):
    statement = ""
    for i in range(n):
        statement += generate_random_value()
        statement += generate_random_boolean_operator()
    statement += generate_random_value()
    return statement, eval(statement)

print("\nBoolean Practice (written by Avikam C.)\nType the answer below each question!")
while True:
    print("\nLevel " + str(difficulty_level))
    for i in range(tests_per_level):
        question, answer = generate_boolean_statement(difficulty_level)
        if input("\n>>> " + question + "\n") == str(answer):
            print("Correct!")
        else:
            print("Wrong, the answer is: " + str(answer))
    difficulty_level += 1
