
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, jsonify

app = Flask(__name__)



from time import gmtime, strftime
from collections import defaultdict
class Chat:
    def __init__(self):
        self.messages = defaultdict(lambda: defaultdict(list))
        self.contacts = defaultdict(list)
        self.history = []

    def otprav(self, kto, komu, chto):
        fchto = f'{strftime("%H-%M-%S")} : {kto} -> {komu} : {chto}'
        self.history.append(fchto)
        self.messages[kto][komu].append(fchto)
        self.messages[komu][kto].append(fchto)

    def pokaji(self, kto, komu):
        return self.messages[kto][komu]

    def dobavkontakt(self, kto, kogo):
        self.contacts[kto].append(kogo)

    def pokajivse(self, kto):
        output = []
        for i in self.messages[kto].values():
            output += i
        return sorted(output)

    def gethistory(self):
        return self.history

    def find(self, target):
        output = []
        for i in self.history:
            if target in i:
                output.append(i)
        return output



chat = Chat()


@app.route('/jonot')
def emil1():
    d = request.args
    chat.otprav(d['kto'], d['komu'], d['chto'])
    output = chat.pokaji(d['kto'], d['komu'])
    return '<br>'.join(output)


@app.route('/tarih')
def hoji():
    return '<br>'.join(chat.gethistory())


@app.route('/tap')
def akyles():
    return '<br>'.join(chat.find(request.args['chto']))




from collections import defaultdict
class Grades:
    def __init__(self):
        self.students = defaultdict(list)

    def addgrade(self, name, grade):
        self.students[name].append(grade)

    def get_avg_grade(self, name):
        return sum(sorted(self.students[name], reverse=True)[:13])/13

    def get_avg_all_students(self):
        output = []
        for name in self.students:
            output.append(f'{name} -> {self.get_avg_grade(name)}')
        return output

    def get_letter_grade(self, grade):
        if grade > 90:
            return 'A'
        elif grade > 80:
            return 'B'
        elif grade > 70:
            return 'C'
        else:
            return 'F'

    def get_all_letter(self):
        output = []
        for name in self.students:
            output.append(f'{name} -> {self.get_letter_grade(self.get_avg_grade(name))}')
        return output




g = Grades()

@app.route('/dobav_otsenku')
def pofig1():
    d = request.args
    name = d['imya']
    grade = int(d['baa'])
    g.addgrade(name, grade)
    return f'Successfully added {name} and {grade}'


@app.route('/otsenki_sifra')
def pofig2():
    return '<br>'.join(g.get_avg_all_students())

@app.route('/otsenki_letter')
def pofig3():
    return '<br>'.join(g.get_all_letter())


app.run()

