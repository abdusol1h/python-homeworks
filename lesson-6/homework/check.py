def check(func):
    def isZero(a, b):
        if b == 0:
            return "Denominator can not be zero"
        return func(a, b)
    return isZero

@check
def div(a, b):
    return a // b 

# test cases
print(div(6, 0))
print(div(6, 3))