def fibonacci(n):
    # 时间复杂度为O(2^N)
    if n < 0:
        return "Incorrect input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def fibonacci_a(n):
    # 空间复杂度为O(N), 使用数组存每一个值, 时间复杂度为O(N)
    if n <= 0:
        return 'Incorrect input'
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        nums = [0] * (n+1)
        nums[0], nums[1] = 0, 1
        i = 2
        while i <= n:
            nums[i] = nums[i-1] + nums[i-2]
            i += 1
        return nums[n-1]

def fibonacci_b(n):
    # 空间复杂度为O(1), 时间复杂度为O(N)
    if n <= 0:
        return 'Incorrect input'
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        while True:
            temp = b
            b = a + b
            a = temp
            n -= 1
            if n <= 2:
                break
        return b
print(fibonacci(5))
print(fibonacci_a(5))
print(fibonacci_b(5))