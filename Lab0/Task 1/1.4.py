with open('input1.txt', 'r') as inputf:
    a, b = map(int, inputf.readline().split())

if -10**9 <= a <= 10**9 and -10**9 <= b <= 10**9:
    with open('output1.txt', 'w') as outputf:
        outputf.write(str(a+b**2))
else:
    print('Одно из чисел вышло за границы')