'''The purpose of this program is to create a class to store the questions,
answer choices, and correct answers for the driver program.'''
class Questions():
    def __init__(self, q, a1, a2, a3, a4, c):
        self.__q = q
        self.__answer1 = a1
        self.__answer2 = a2
        self.__answer3 = a3
        self.__answer4 = a4
        self.__correct = c
        
    def getquestion(self):
        return self.__q
    def getanswer1(self):
        return self.__answer1
    def getanswer2(self):
        return self.__answer2
    def getanswer3(self):
        return self.__answer3
    def getanswer4(self):
        return self.__answer4
    def getcorrect(self):
        return self.__correct
