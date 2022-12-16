dog = {'lilly': 'kendall'}
cat = {'nevil': 'sophie'}
snake = {'pycharm': 'maury'}


pets = [dog, cat, snake]
for pet in pets:
    for name, owner in pet.items():
        print(f"{owner.title()} owns {name.title()}")
