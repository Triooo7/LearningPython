
def listcomparision():
    list1 = [1,2,3,4]
    list2 = [3,4,5,6]
    answer = []

    x = [item for item in list1 if item in list2]
    answer.append(x)
    print(answer)

def listcomparision_two():
    list3 = ["Elie", "Tim", "Matt"]
    answer2 = []
    for word in list3:
        answer2.append(word[::-1].lower())
        print(answer2)



if __name__ == '__main__':
    listcomparision()
    listcomparision_two()
