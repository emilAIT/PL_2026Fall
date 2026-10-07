class Grade:
    def createGrade(self, score):
        pass


class LetterGrade(Grade):
    def createGrade(self, score):
        if score > 90:
            return 'A'
        elif score > 80:
            return 'B'
        elif score > 70: 
            return 'C'
        else:
            return 'F'

class PassFailGrade(Grade):
    def createGrade(self, score):
        if score > 70:
            return 'P'
        else:
            return 'F'


class Course:
    def createGrader(self):
        pass

    def getScore(self, score):
        return self.createGrader().createGrade(score)


class LetterCourse(Course):
    def createGrader(self):
        return LetterGrade()

class PassFailCourse(Course):
    def createGrader(self):
        return PassFailGrade()


class DifferentGrade(Grade):
    def createGrade(self, score):
        return 'F'

class StupidCourse(Course):
    def createGrader(self):
        return DifferentGrade()




class StupidCourse2:
    def getScore(self, score):
        return 'F'


pl = LetterCourse()
print('Score for 90 is = ', pl.getScore(90))
manasovedenia = PassFailCourse()
print('Score for 70 is = ', manasovedenia.getScore(70))

quantum = StupidCourse()
print('Score for 70 is = ', quantum.getScore(70))

quantum2 = StupidCourse2()
print('Score for 70 is = ', quantum2.getScore(70))