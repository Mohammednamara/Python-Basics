
#Simple condition
x=2
if x>4:
    print("x > 4")
else:
    print(x)
------
x=4
if x==3:
    print('x=3')
elif x==4:
    print('x=4')
else:
    print(x)
--------
#Nested If
x=9
if x<10:
    print('x<10')
    if x<5:
        print('x<5')
    else:
        print('x>5')
else:
    print('x>10')
-----
#If with Boolean Operators
name="Namara"
age=29
if name == "Namara" and age ==29:
    print("Welcome Namara")
if name =="Namara" or age== 40:
    print("Hello Namara")
