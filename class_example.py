# class example

class MyClass:
    number = 0
    name = 'noname'
    age = 'under 40'

def Main():
    me = MyClass()
    me.number = 55
    me.name = 'Martin'
    me.age = 40

    friend = MyClass()
    friend.number = 10
    friend.name = 'Susan'
    friend.age = 25

    default = MyClass()


    print('My name is ' + me.name + ' I am ' + str(me.age) + ' and my number is: ' + str(me.number))
    print('My name is ' + friend.name + ' I am ' + str(friend.age) + ' and my number is: ' + str(friend.number))
    print('My name is ' + default.name + ' I am ' + str(default.age) + ' and my number is: ' + str(default.number))
    

Main() 
    


    
