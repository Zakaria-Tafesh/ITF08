
# age = 15
# city = 'Gaza'
#
# if age >= 18:
#     print('Age is more than 18')
#     if city == 'Gaza':
#         print('Full Access')
#     elif age > 20:
#         print('Age is more than 20')
#
#     if city == 'Rafah':
#         print('City is Rafah ')
#     else:
#         print('City is not Rafah')
#
#     print('End of the first If statement')
#
# elif age >= 10:
#     print('Age is between 10 and 17')
#
# elif age >= 7:
#     print('Age is between 7 and 9')
#
#
# print('End of the Code')


def get_mark(mark):

    if 90 <= mark <= 100:
        return 'A'
    elif mark >= 80:
        return 'B'

    elif mark >= 70:
        return 'C'

    elif mark >= 60:
        return 'D'
    else:
        return 'F'

    print('End of the function')


m = 75
var = get_mark(40)
print(var)
