def is_power(a, b):
    if a == b: # base case
        return True
    elif a % b != 0 or a == 0: # a == 0 is required otherwise the function will recurse forever
        return False
    else:
        return is_power(a/b, b)

print(is_power(0,1))
print(is_power(9,2))
