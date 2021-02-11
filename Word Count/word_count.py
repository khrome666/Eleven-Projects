again = True
while again:
    on_your_mind = input('What\'s on you mind today?')
    words = on_your_mind.split()
    print(f'Oh, nice! You just told me what\'s on your mind in {len(words)} word{"" if len(words) == 1 else "s"}!')
    again = input('Again (y/n)?').lower()[0] == 'y'
