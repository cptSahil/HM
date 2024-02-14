def fibonacci(n):
    num1, num2 = 0, 1
    count = 0
    fib = []
    if n <= 0:
        return "Please enter a positive integer!"
    elif n == 1:
        fib.append(num1)
    else:
        while count < n:
            fib.append(num1)
            nth = num1 + num2 
            num1 = num2
            num2 = nth
            count += 1
    return fib

if __name__ == "__main__":
    input_value = int(input("Enter the number: "))
    print(fibonacci(input_value))
