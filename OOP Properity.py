class Student:
    def __init__(self, name, lastname, university_nick):
        self.name = name
        self._lastname = lastname
        self.__university = university_nick

    @property
    def fullname(self):
        return '{} {}'.format(self.name, self._lastname)

    @fullname.setter
    def fullname(self, name):
        result = name.split()
        self.name = result[0]
        self._lastname = result[1]

    @property
    def email(self):
        return f'{self.name.lower()}.{self._lastname.lower()}@{self.__university.lower()}.edu.ge'

    def get_university(self):
        return self.__university


class Person(Student):
    def __init__(self, name, lastname, university_nick, person_count):
        super().__init__(name, lastname, university_nick)
        self._person_count = person_count

    @property
    def email(self):
        return f'{self.name.lower()}.{self._lastname.lower()}.{self._person_count}@{self.get_university().lower()}.edu.ge'


st1 = Student('giorgi', 'duchidze', 'btu')
st2 = Person('demetre', 'natidze', 'stu', 1)
print(st1.email)
print(st2.email)
print(st1.get_university())
