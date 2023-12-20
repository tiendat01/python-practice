# def <function_name>(params):
#     # code

def fib(n):
    """Print a Fibonacci series up to n."""  # docstring
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()  # endline


# call function:
fib(2000)

# default argument

# L is  mutable object


def f(a, L=[]):
    L.append(a)
    return L


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f(1))
print(f.__defaults__)
print(f(2))
print(f(3))
