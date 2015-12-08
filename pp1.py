class hello(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def print_name(self):
        print('%s, %s, %s'%(self.name, self.age, self.score))

    def get_grade(self):

        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 70:
            return 'C'
        else:
            return 'D'



h = hello('Bond', 22, 99)
s = hello('Wanghao', 21, 150)
h.print_name()
s.print_name()
print(s.get_grade())
print(h.get_grade())