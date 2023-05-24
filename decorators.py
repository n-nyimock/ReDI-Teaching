def justice(fun):
    def wrapper(k, l):
        print(f"Calling function: {fun.__name__}")
        result = fun(k, l)
        print(f"Function {fun.__name__} finished")
        return result
    return wrapper

@justice
def add_numbers(a, b):
    return a + b

def prime_numbers(c, d):
    return c*d

result = add_numbers(3, 5)  # Calling function: add_numbers
                            # Function add_numbers finished
print(result)  # 8

result1 = prime_numbers(3, 17)
print(result1)
