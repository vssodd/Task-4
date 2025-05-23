place = int(input('Enter your admission place: '))

if place <= 10:
    points = int(input('Enter your exam points: '))
    print('Congratulations, you are admitted!')
    if points >= 290:
        print('You will receive a scholarship bonus.')
    else:
        print('Unfortunately, you did not qualify for a scholarship.')
else:
    print('You were not admitted.')
