import time
t_start = time.perf_counter()

def last_digit(n):
    if 0 <= n <= 10**7:
        pisano_p = 60
        def fib_mod(m):
            previous, current = 0, 1
            for i in range(m):
                previous, current = current, (previous + current) % 10
            return previous
        n_mod = n % pisano_p

        return fib_mod(n_mod)
    else:
        print('Число n вышло за границы допустимого значения')

file = open('input3.txt', 'r').read().strip()
num = int(file)
res = open('output3.txt', 'w').write(str(last_digit(num)))

print('Время работы %s секунд' % (time.perf_counter() - t_start))