def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
n = 5
result = factorial_iterative(n)
print(f"The factorial of {n} is {result}")

