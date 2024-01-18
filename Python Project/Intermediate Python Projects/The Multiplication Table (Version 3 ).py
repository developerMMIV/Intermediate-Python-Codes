while True:
    print("This is the version 3 of the multiplication table ")
    print('-'*30)
    n = int(input('What number should i show the multiples?:'))
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n}X{c}={n*c}')
    print('-'*30)
print('End of the show')
