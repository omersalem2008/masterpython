# ------------------------------------------------------
# -- Advanced_Lessons => Timing Your Code With Timeit --
# ------------------------------------------------------
# - timeit: - Get Execution Time Of Code By Running 1M (million) Time And Give You Minimal Time
# -         - It Used For Performance By Testing All Functionality
# - timeit(stmt, setup, timer, number)
# - timeit(pass, pass, default, 1.000.000) Default Values
# -------------------------------------------------------
# - stmt: Code You Want To Measure The Execution Time
# - setup: Setup Done Before The Code Execution (Import Module Or Anything)
# - timer: The Timer Value
# - number: How Many Execution That Will Run
# -------------------------------------------------------
# so this is very useful for performance testing
# -------------------------------------------------------
import re
import timeit

print(dir(timeit))

print(timeit.timeit("'Elzero' * 1000")) # here the stmt is "'Elzero' * 1000" and the setup is empty
# and the other values are default values


# name = "Elzero"

# print(name * 1000)

print(timeit.timeit("name = 'Elzero'; name * 1000")) # here the stmt is "name = 'Elzero'; name * 1000"
# and the other values are default values and we put ; after the name = 'Elzero' line to make 
# two commands in one line

# print(random.randint(0, 50))

print(timeit.timeit(stmt="random.randint(0, 50)", setup="import random"))
# here because we are using random module we need to import it in the setup
# and the other values are default values so if we didnt import the random module in the setup
# it will give us an error

print(timeit.repeat(stmt="random.randint(0, 50)", setup="import random", repeat=4))
# here we are using repeat to repeat the code 4 times and it will give us a list of 4 values
# and the values are the time it took to execute the code
# the result will be like this:
# [0.000123456, 0.000123456, 0.000123456, 0.000123456]
from timeit import repeat, timeit as ti

def test(no):
    if no > 0:
        return "positive"
    else:
        return "negative"

print(repeat(stmt="test(5)", setup="from __main__ import test", repeat=3))
# we put setup="from __main__ import test" to import the test function and 
# if we dont put it it will give us an error so any function or class
# we want to use in the stmt we have to import it in the setup


print(ti(stmt="no=1; print('positive' if no > 0 else 'negative')", number=3))

#here number=3 means that the code will run 3 times and the result will be:
# positive
# positive
# positive

