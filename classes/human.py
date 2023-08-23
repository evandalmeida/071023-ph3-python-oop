class Human:
    def __init__ (self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self._age = 0

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __repr__(self):
        return f'Hi my name is {self.full_name()}, I\'am {self._age} years-old.'
    
    def happy_bday(self):
        self._age += 1
        return self._age

    @property
    def age(self):
        return f'{self.full_name()} is {self._age}'
    
    @age.setter
    def age(self, value):
        if type (new_age) == int:
            self._age = new_age
        else:
            print('Enter a number please')
