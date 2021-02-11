again = True
while again:
    try:
        print('What number are you thinking?')
        number = int(input())
        odd_or_even_number = 'odd' if number % 2 else 'even'
        print(f'That\'s an {odd_or_even_number} number. Have another?')
        again = input()[0].lower() == 'y'
    except:
        print('That is not a valid number! Try again.')
