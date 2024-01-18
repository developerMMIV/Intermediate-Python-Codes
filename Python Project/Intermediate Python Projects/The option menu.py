from time import sleep
n1 = int(input('Digit 1:'))
n2 = int(input('Digit 2:'))
option = 0

while option !=5:
    print('''    [ 1 ] Add
    [ 2 ]  Multiply
    [ 3 ] The largest number
    [ 4 ] new numbers 
    [ 5 ] Leave the program''')
    option = int(input('>>>>>>>>What is your option?'))
    if option ==1:
        add = n1 + n2
        print('The sum between {} and {} is {} '.format(n1,n2,add))
    elif option ==2:
        product = n1 * n2
        print('The product between {} and {} is {} '.format(n1,n2,product))
    elif option ==3:
        if n1 > n2:
            maior = n1
        else:
            maior =n2
        print('The largest number between {} and {} is {}'.format(n1,n2,maior))
    elif option== 4:
        print(' Inform the two numbers again')
        n1 = int(input('digit 1:'))
        n2 = int(input('digit 2:'))
    elif option ==5:
        print("Ending the program.................")
    else:
        print('Invalid Option, try again')
    print('=-='*10)
    sleep(1)
print('End of the program ')



print('Goodbye')