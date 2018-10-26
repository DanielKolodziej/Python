import time

def fib(n):
    return n if n < 2 else fib(n-2) + fib(n-1)

fib_cache = {}
def fibm(n):
    if n in fib_cache:
        return fib_cache[n]
    else:
        fib_cache[n] = n if n < 2 else fibm(n-2) + fibm(n-1)
        return fib_cache[n]

startTime = time.clock()

print("Test w/o Memoization" , fib(35))

endTime = time.clock()

print("Time lapse",endTime-startTime)


nstartTime = time.clock()

print("Test w Memoization" , fibm(35))

nendTime = time.clock()

print("Time lapse",nendTime-nstartTime)
