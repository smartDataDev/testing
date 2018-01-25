'''
name = 'Bob'
if name == 'Bob':
    print ( 'Hi ' + name)
print ('Done')
'''

print ('How many cars do you have ?')
numCars = input()
try:
    if int(numCars) > 2:
        print ('Why do you need so many cars ?')
    elif 1 <= int(numCars) <= 2:
        print ('Ok ')
    else:
        print ('So you do not have any car ?')
except:
    print ('Please enter a number: ')


           
