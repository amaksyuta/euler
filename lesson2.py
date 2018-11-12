print("[INFO]: Fibonacci sequence task")
#F0 = 0
#F1 = 1
#Fn = Fn-1 + Fn-2
#############################################################
def get_fib_numbers(n):
    """Function for returning Fibonacci number"""
    l = [0, 1]
    for i in range(2, n + 1):
        l.append(l[i-1] + l[i-2])
    return l
#############################################################
def get_fib_summ(l):
    """Function for return summa of elements Fibonacci"""
    return sum(n for n in l if n % 2 == 0)
#############################################################
def fib(n):
    if n in M:
        return M[n]
    M[n] = fib(n - 1) + fib(n - 2)
    return M[n]
#############################################################
def fib1(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a
#############################################################
n = 10
#a = get_fib_summ(get_fib_numbers(n))

M = {0: 0, 1: 1}


a = fib1(n)
for i in range(a):
    print(i)


