from abc import abstractclassmethod


again = True
while again:
    full_version = input('Enter the full description of an organization or concept:')
    acronym = ''.join(w[0] for w in full_version.split()].upper()
    print(f'The acronym is: {acronym}')
    again = input('Again (y/n)?').lower()[0] == 'y'
