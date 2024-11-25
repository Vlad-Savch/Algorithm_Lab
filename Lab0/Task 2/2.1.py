import time
t_start = time.perf_counter()
def fib(n):
    if 0 <= n <= 45:
        previous, current = 0, 1
        for i in range(n):
            previous, current = current, previous + current
        return previous
    else:
        print('Число n вышло за границы допустимого значения')

file = open('input2.txt', 'r').read().strip()
num = int(file)
res = open('output2.txt', 'w').write(str(fib(num)))

print('Время работы %s секунд' % (time.perf_counter() - t_start))