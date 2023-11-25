import math
def calculate_square_root(number):
    return math.sqrt(number)
if __name__ == "__main__":
    num = float(input("Enter a number: "))
    result = calculate_square_root(num)
    print(f"The square root of {num} is {result}")
