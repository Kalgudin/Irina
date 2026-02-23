

class Pers:
    def __init__(self, n='Jon Dow', a=20):
        self.name = n
        self.age = a
    def about(self):
        print(f'Name - {self.name} \nAge - {self.age}')

class Teacher(Pers):
    def __init__(self, n='Jon Dow', s='Dow', p='Professor',  a=20):
        super().__init__(n, a)
        self.surname = s
        self.prof = p
    def about(self):
        print(f'Name - {self.name} {self.surname} \nProfesion - {self.prof} \nAge - {self.age}')

p = Pers('Nick', 45)
p.about()

t = Teacher('Vas', a=55, p='Doc', s="Puprin")
t.about()
