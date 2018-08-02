import numpy as np
check = 'Y'
while ( check == 'Y'):
    #start here
    x=input('Enter a number from 1 to 50: ')
    y=np.random.randint(1,51)
    if ( x == y ):
        #If start here
        print('It is your lucky day')
    else:
        print('Better luck next time!!!')
    print('Your number: {}'.format(x))
    print('My number: {}'.format(y))
    check = input('Do you want to continue, if Yes enter "Y"')
