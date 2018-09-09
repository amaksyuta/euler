print("\n[INFO]:First EULER lesson with function")
def calculMultipleNumbers(number):
    """Function for return Summary of some numbers range"""
    return sum(n for n in range(number) if n % 3 == 0 or n % 5 == 0)

num = 1000
summa = calculMultipleNumbers(num)
print("\n[INFO]: Result summa is ", summa)