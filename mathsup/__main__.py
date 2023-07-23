import argparse
import core

def main():
    parser = argparse.ArgumentParser(description="Calculate the factorial of a number.")
    parser.add_argument("--number", "-n", type=int, help="The number for which to calculate the factorial.")
    args = parser.parse_args()

    if args.number:
        result = core.factorial(args.number)
        print(f"The factorial of {args.number} is {result}.")



if __name__ == "__main__":
    main()