experience = int(input('Enter your experience points: '))
initial_level = 1

if 1000 <= experience < 2500:
    print('Your level:', initial_level + 1)
elif experience < 5000:
    print('Your level:', initial_level + 2)
elif experience <= 10000:
    print('Your level:', initial_level + 3)
else:
    print('Maximum level reached!')
