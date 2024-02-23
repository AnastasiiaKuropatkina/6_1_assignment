import argparse
import sys

parser = argparse.ArgumentParser(description="Simple CLI Calculator")
parser.add_argument('num1', type=int)
parser.add_argument('symbol', choices=['+', '-', '/'])
parser.add_argument('num2', type=int)
args = parser.parse_args()


if args.symbol == '+':
    result = args.num1 + args.num2
elif args.symbol == '-':
    result = args.num1 - args.num2
elif args.symbol == '/':
    result = args.num1 / args.num2
else:
    print("Unsupported operation")
    sys.exit(1)


print(f"The result is {result}")