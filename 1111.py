import random

letters = "abcdefjhijklmnopqrstuvwxyz"
randomletters = ""


def generateletters(randomletters):
    randomint = random.randint(1, 10)
    for i in range(randomint):
        randomnum = random.randint(0, len(letters) - 1)
        randomletters = randomletters + letters[randomnum]
    return randomletters

def validateAnswer(randomletters, answer):

    for letter in answer:
        if letter not in randomletters:
            return "Invalid answer"
        else:
            pass

    return len(answer)



# def validateAnswer(randomLetters, answer):
#     for letters in answer:
#         if letters not in randomLetters:
#             return 0
#         else:
#             pass
    
#     return len(answer)

generated = generateletters(randomletters)
print(generated)

answer = input("Enter your answer: ")

print(validateAnswer(generated, answer))