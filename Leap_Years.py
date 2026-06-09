f_year = int(input('Enter first year:'))
s_year = int(input('Enter second year:'))

for year in range(f_year,s_year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year!")
    else:
        print(f'{year} is not a leap year.')