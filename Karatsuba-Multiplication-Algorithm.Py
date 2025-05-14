def karatsuba(x, y):
    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)

    n = max(len(x), len(y))
    x = x.zfill(n)
    y = y.zfill(n)

    m = n // 2
    x_high, x_low = x[:m], x[m:]
    y_high, y_low = y[:m], y[m:]

    a = karatsuba(x_high, y_high)
    b = karatsuba(x_low, y_low)
    c = karatsuba(str(int(x_high) + int(x_low)), str(int(y_high) + int(y_low))) - a - b

    result = a * 10**(2 * m) + c * 10**m + b
    return result

# 64-digit numbers
num1 = "3141592653589793238462643383279502884197169399375105820974944592"
num2 = "2718281828459045235360287471352662497757247093699959574966967627"

result = karatsuba(num1, num2)

print(result)
