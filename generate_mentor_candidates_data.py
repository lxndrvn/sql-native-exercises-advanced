"""
puts 10,000 (yep, TEN THOUSAND) records into the mentor_candidates table
  - first_name possible values are: Miklós, Tamás, Dániel, Mateusz, Attila, Pál, Sándor, Prezmek, John, Tim, Matthew, Andy, Giancarlo
  - last_name possible values are: Beöthy, Tompa, Salamon, Ostafil, Molnár, Monoczki, Szodoray, Ciacka, Carrey, Obama, Lebron, Hamilton, Fisichella
  - birth_year should be between 1960-1995
  - email should be a random, but valid email
  - city possible values are: Budapest, Miskolc, Krakow, Barcelona, New York
  - phone_number should be a random 10 digit number, with a plus sign at the beginnin
  - level should be between 1-10
- does all of this in a transaction
"""
import random

def first_name():
    return random.choice(
        ['Miklós', 'Tamás', 'Dániel', 'Mateusz', 'Attila', 'Pál', 'Sándor', 'Prezmek', 'John', 'Tim',
        'Matthew', 'Andy', 'Giancarlo']
    )


def last_name():
    return random.choice(
        ['Beöthy', 'Tompa', 'Salamon', 'Ostafil', 'Molnár', 'Monoczki', 'Szodoray', 'Ciacka', 'Carrey',
         'Obama', 'Lebron', 'Hamilton', 'Fisichella']
    )


def birth_year():
    return str(random.randint(1960, 1995))


def email(first_name, last_name, birth_year):
    return '{}{}{}@codecool.com'.format(first_name[0].lower(), last_name[0].lower(), birth_year)


def city():
    return random.choice(['Budapest', 'Miskolc', 'Krakow', 'Barcelona', 'New York'])


def phone_number():
    numbers = []
    for n in range(10):
        number = random.randint(0,10)
        numbers.append(str(number))
    return '+' + ''.join(numbers)


def level():
    return str(random.randint(1,11))


def sql_line():
    f = first_name()
    l = last_name()
    b = birth_year()
    line = '''INSERT INTO \"mentor_candidates\" (first_name, last_name, birth_year, email, city, phone_number, level)
    VALUES ('{}','{}','{}','{}','{}','{}','{}');\n'''.format(f, l, b, email(f, l, b), city(), phone_number(), level())
    return line

def run():
    with open ('1-fake-mentor-candidates.sql', 'w') as datafile:
        for line in range(10000):
            line = sql_line()
            datafile.write(line)
        datafile.write("END TRANSACTION;")

run()

