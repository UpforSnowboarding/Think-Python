import math

def eval_loop():
    while True:
        a = input("Enter something for python to evaluate: ")
        if a == 'done':
            break
        else:
            result = eval(a)
            print(result)
    print(a)

eval_loop()




# cleaner version with try and except to catch errors

def eval_loop2():
    while True:
        a = input("Enter something for python to evaluate: ")
        try:
            print(eval(a))
        except:

            if a == 'done':
                break
            else:
                print(a)

