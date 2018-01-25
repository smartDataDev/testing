# random/sys example

import random


x = random.randint(10, 20)
if x == 15:
    print ('You are winner !')
elif x <= 14:
    print ('Sorry, you are below the target. Try again ...')
elif x >= 16:
    print ('Sorry, you are above the target. Try again ...')

else:
    print ('You almost there. Please try again ... ')

    
'''
import sys
print ('Hello')
sys.exit()
print ('You will not see it') 
'''
