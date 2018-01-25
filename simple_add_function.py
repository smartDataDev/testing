# simple add function

def simple_add_function(x,y,z):
    xyz_sum = int(x) + int(y) + int(z)
    
    print ('Your final scope of math,english and art is: ', str(xyz_sum))
    if xyz_sum > 100:
        print ('You are the winner !!!')
    elif xyz_sum == 100:
        print ('You have 100 pts !!')
    elif 100 > xyz_sum >= 90:
        print ('Very good !')
    elif 90 > xyz_sum >= 80:
        print ('Good !')
    else:
        print (' You have below 80 pts , try again ... ')

    
# simple_add_function(x,y,z)


print (' Enter math,english and art test pts values:')
print ('Enter math score:')
x = input()
print ('Enter english score:')
y = input()
print ('Enter art score:')
z = input()

simple_add_function(x,y,z)
    
