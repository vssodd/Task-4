rating = int(input('What grade did you get in math? '))

if rating == 2 or rating == 3:
    print('Not good. Go study!')
elif rating == 4 or rating == 5:
    print('Well done! You can relax.')
else:
    print('Invalid grade entered.')
