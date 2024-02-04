# mail generator program

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
        return f'{self.name}.{self._lastname}@{self.__university}.edu.ge'

# Example usage
st1 = Student('giorgi', 'duchidze', 'btu')
print(st1.email)

