def fibonacci(n):
    if n < 0:
        print("Input should be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
def main():
   
    terms = input("Enter the term you want to calculate in the Fibonacci series: ")
    try:
        n = int(terms)
        result = fibonacci(n)
        print(f"Fibonacci({n}) = {result}")
    except ValueError:
        print("Please enter a valid non-negative integer.")

if __name__ == "__main__":
    main()
