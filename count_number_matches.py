number_1 = int(input('Enter the first number: '))
number_2 = int(input('Enter the second number: '))
number_3 = int(input('Enter the third number: '))

if number_1 == number_2 == number_3:
    print('Matches found: 3')
elif number_1 == number_2 or number_2 == number_3 or number_1 == number_3:
    print('Matches found: 2')
else:
    print('Matches found: 0')
