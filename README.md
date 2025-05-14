# Karatsuba-Multiplication-Algorithm

# Description

This Python script implements the Karatsuba multiplication algorithm, an efficient method for multiplying large numbers. The algorithm works by recursively splitting the numbers into smaller parts, performing multiplications on them, and combining the results. It reduces the complexity of multiplication from O(n2)O(n2) to O(nlog⁡23)O(nlog2​3), making it much faster for large numbers compared to traditional multiplication methods.

# Usage
Example
```
def karatsuba(x, y):
    # Base case: single-digit multiplication
    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)

    # Making the lengths of x and y equal
    n = max(len(x), len(y))
    x = x.zfill(n)
    y = y.zfill(n)

    # Splitting the numbers
    m = n // 2
    x_high, x_low = x[:m], x[m:]
    y_high, y_low = y[:m], y[m:]

    # Recursive steps
    a = karatsuba(x_high, y_high)
    b = karatsuba(x_low, y_low)
    c = karatsuba(str(int(x_high) + int(x_low)), str(int(y_high) + int(y_low))) - a - b

    # Combining results
    result = a * 10**(2 * m) + c * 10**m + b
    return result

# 64-digit numbers
num1 = "3141592653589793238462643383279502884197169399375105820974944592"
num2 = "2718281828459045235360287471352662497757247093699959574966967627"

# Multiply the numbers using Karatsuba's algorithm
result = karatsuba(num1, num2)

# Print the result
print(result)

```

Output

8539652321666725323973357046576183724801908225319472645116508051551424545322670232461593655038415456722186322481170720289173184


# Function Descriptions
karatsuba(x, y)

This function multiplies two large numbers represented as strings x and y using the Karatsuba algorithm. It recursively splits the numbers, performs smaller multiplications, and combines the results to get the final product.
# Applications

* Multiplication of large numbers in cryptography and data encryption
* High-performance computing tasks requiring fast multiplication of integers
* Educational purposes for demonstrating divide-and-conquer algorithms

# License

*  This project is licensed under the MIT License.
