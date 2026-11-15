try:
    age=int(input('enter your age'))
except:
    print('please enter an valid value')
else:
    print('age value taken succesfully')
finally:
    print('this is a program which takes your age')            