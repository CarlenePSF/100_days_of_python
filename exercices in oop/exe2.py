"""
2. Write a Python program to create a person class. Include attributes like name,
 country and date of birth. Implement a method to determine the person's age.
"""
from datetime import date, datetime


class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def determine_age(self):
        curret_year = date.today().year
        year_of_birth = datetime.strptime(self.date_of_birth, '%Y-%m-%d').year
        return curret_year - year_of_birth



if __name__ == '__main__':
    person_1 = Person("Bob", "USA", "1999-01-01")
    print('Name:', person_1.name, 'Country:', person_1.country, "Date of birth:", person_1.date_of_birth)
    print("Person's age:", person_1.determine_age())