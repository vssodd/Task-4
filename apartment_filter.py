price = int(input('Enter the apartment price: '))
yardage = int(input('Enter the apartment size (sqm): '))

if yardage >= 100 and price <= 10_000_000:
    print('The apartment is suitable!')
elif yardage >= 80 and price <= 7_000_000:
    print('The apartment is suitable!')
else:
    print('The apartment is not suitable.')
