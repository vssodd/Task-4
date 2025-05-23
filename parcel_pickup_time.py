# Check if a parcel can be received at a given hour

time = int(input('Enter the time from 0 to 23 hours: '))

if (0 <= time < 8) or (10 <= time < 12) or (14 <= time < 15) or (18 <= time < 20) or (22 <= time <= 24):
    print('You cannot receive the parcel.')
else:
    print('You can receive the parcel!')
