
# Loops
# print('Hello')
# print('Hello')
# print('Hello')
# print('Hello')
# print('Hello')
# a = int(input('Enter Num:\n'))
# for x in range(11):
#     result = x * a
#     print(f'{a} * {x} = {result}')
# word = input('Enter a Word: ')
# for c in word:
#     print(c, end='#')
# for c in 'Noor':
#     print(c)

# print('N', 'o', 'o', 'r', sep='#', end='$$$$$')
# print('End')
# print('o')
# print('r')


# While
# i = 1
# while i <= 5:
#     print(i)
#     i += 1  # i = i + 1
# row = 5
# for x in range(1, row + 1):
#     for y in range(x):
#         print(x, end='')
#     print()

for i in range(2, 20):
    print('###')
    if i == 5 or i == 7:
        continue
    print(i)
    if i == 15:
        break

