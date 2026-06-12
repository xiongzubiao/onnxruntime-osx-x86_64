import argparse

def fizzbuzz(n):
    """
    Returns 'Fizz' if n is divisible by 3, 'Buzz' if n is divisible by 5,
    'FizzBuzz' if n is divisible by both 3 and 5, or the number as a string.
    """
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

def main():
    parser = argparse.ArgumentParser(description="Standard FizzBuzz script.")
    parser.add_argument("--limit", type=int, default=20, help="Upper limit for FizzBuzz (default: 20)")
    args = parser.parse_args()

    # Default requirement: run for 1..20
    for i in range(1, args.limit + 1):
        print(fizzbuzz(i))

if __name__ == "__main__":
    main()
