gender = str(input('What is your gender?[M/F]')).strip().upper()[0]
while gender not in 'MmFf':
    gender= str(input('invalid input, try again')).strip().upper()[0]
print('the {} gender registered successfully'.format(gender))
