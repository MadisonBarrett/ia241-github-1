'''
lab 5
'''

#3.1

alien_color= 'green'

if alien_color == 'red':
    print('you have earned 5 points')
    
#3.2
    
if alien_color == 'green':
    print('you have earned 5 points')
else:
    print('you have earned 10 points')
    
#3.3

favorite_fruits= [ 'apple', 'banana', 'orange']

if 'mango' in favorite_fruits:
    print('you really like mango')
    
if 'kiwi' in favorite_fruits:
    print('you really like kiwi')
    
if 'apple' in favorite_fruits:
    print('you really like apples')
    
#3.4

age=53

if age<10:
    print('kid')
    
elif 10<=age<20:
    print('teenager')
    
elif 20<=age<65:
    print('adult')
    
else:
    print('elder')