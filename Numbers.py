
def lol():
    new_list = ["Elie", "Tim", "Matt"]
    answers = []
    for letters in new_list:
        letter = letters[:1]
        answers.append(letter)
    print(answers)

def rofl():
    answers2 = []
    numbers = [1,2,3,4,5,6]
    x = [num for num in numbers if num % 2 == 0]
    answers2.append(x)
    print(answers2)



if __name__ == '__main__':
    lol()
    rofl()

