# year = int(input("Please, Input the Year:\n"))
# age = 2023 - year
# new_age = age - 2
# print(f'Hello, Your Age is: {new_age}')
#
# year2 = int(input("Please, Input the Year:\n"))
# age2 = 2023 - year2
# new_age2 = age2 - 2
# print(f'Hello, Your Age is: {new_age2}')


def print_hello(name, age, city='Gaza'):
    age = age + 10
    print(f"Hello {name}!")
    print(f"Your age is {age}")
    print(f"Your City is {city}")
    print('#'*50)
    get_age(2000)
    return 10
    # print('Batata')


def get_age():
    def get_year_from_user():
        year_input = int(input('Input the Year:\n'))
        return year_input

    year = get_year_from_user()
    age_year = 2023 - year
    print('Age is ' + str(age_year))
    return age_year


age2 = get_age()
age3 = get_age()
# print_hello('Noor', 20, 'Rafah')
# print_hello('Doaa', 22)
# print(age2)

# print(age2)
# print(print_hello('Noor'))
# print_hello('Reem')
# print_hello('Ahed')

